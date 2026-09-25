@echo off
chcp 65001 > nul
title Gerador de Recibos Automatizado 🧾

REM Tenta executar usando python no PATH
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python main.py
    pause
    exit /b
)

REM Tenta executar via caminho padrão do Python 3.11 instalado
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" main.py
    pause
    exit /b
)

REM Tenta executar via caminho padrão do Python 3.13 instalado
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" main.py
    pause
    exit /b
)

echo [ERRO] Python não foi encontrado no sistema.
echo Verifique se o Python 3 está instalado corretamente.
pause
