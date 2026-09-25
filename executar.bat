@echo off
setlocal
chcp 65001 >nul

REM Verifica o Python oficial instalado no LocalAppData
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" "%~dp0main.py"
    goto fim
)

if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%~dp0main.py"
    goto fim
)

REM Tenta o inicializador padrao py
py -3 "%~dp0main.py" 2>nul
if %ERRORLEVEL% EQU 0 goto fim

REM Tenta comando python direto
python "%~dp0main.py" 2>nul
if %ERRORLEVEL% EQU 0 goto fim

echo.
echo [ERRO] Python 3 nao foi encontrado no seu computador.
echo Verifique se o Python esta instalado.
echo.

:fim
pause