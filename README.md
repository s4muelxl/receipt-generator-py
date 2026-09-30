<div align="center">

# 🧾 Gerador de Recibos Automatizado (Python CLI)

**Uma solução leve, ágil e sem dependências externas para gerar comprovantes e recibos de vendas profissionais prontos para WhatsApp e e-mail.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)]()

[Funcionalidades](#-funcionalidades) •
[Como Usar](#-como-usar) •
[Exemplo Visual](#-exemplo-de-recibo-gerado) •
[Estrutura](#-estrutura-do-projeto) •
[Autor](#-autor)

</div>

---

## 💡 Sobre o Projeto

No dia a dia do comércio e de prestadores de serviço autônomos, fechar vendas pelo **WhatsApp ou redes sociais** exige velocidade e clareza. Preencher recibos à mão ou digitar mensagens soltas consome tempo e abre margem para erros de cálculo.

O **Gerador de Recibos Automatizado** foi desenvolvido para resolver essa dor:
- Elimina erros de cálculo manuais.
- Padroniza a comunicação visual com o cliente, transmitindo mais credibilidade.
- Salva um histórico em arquivos `.txt` organizados por cliente e data.
- **Zero instalação de bibliotecas:** roda nativamente em qualquer máquina com Python instalado.

---

## ✨ Funcionalidades

- 🛒 **Inserção Dinâmica de Itens:** Adicione quantos produtos ou serviços quiser no mesmo recibo com controle de quantidade e valor unitário.
- 💰 **Cálculo Automático & Moeda:** Subtotais por produto, quebra de valores e soma total calculados automaticamente no formato padrão brasileiro (`R$ 0,00`).
- 🛡️ **Validação e Tratamento de Erros:** Aceita valores com vírgula ou ponto (ex: `29,90` ou `29.90`) e previne valores negativos ou entradas inválidas.
- 🆔 **Identificador e Timestamp Único:** Cada recibo ganha data/hora exata e uma numeração exclusiva (`#YYYYMMDD-HHMMSS`).
- 📂 **Exportação Automática em UTF-8:** Gera um arquivo de texto limpo dentro da pasta `recibos/`, pronto para abrir, copiar e enviar.
- ⚡ **Execução com 1 Clique (Windows):** Acompanha script executável (`executar.bat`) para quem prefere não abrir o terminal manualmente.

---

## 📄 Exemplo de Recibo Gerado

Ao finalizar a inserção dos dados, o recibo é exibido no terminal e salvo em arquivo com a seguinte formatação:

```text
==================================================
         COMPROVANTE / RECIBO DE PEDIDO         
==================================================
Data/Hora : 25/09/2026 às 17:15:20
Recibo Nº : #20260925-171520
Cliente   : João Silva
Contato   : (11) 98765-4321
Pagamento : Pix
--------------------------------------------------
QTD   DESCRIÇÃO                               TOTAL
--------------------------------------------------
2x    Camiseta Algodão                     R$ 119,80
     (2x de R$ 59,90)
1x    Boné Aba Reta                        R$  49,90
--------------------------------------------------
VALOR TOTAL:                               R$ 169,70
--------------------------------------------------
Observações: Entrega via Sedex.
--------------------------------------------------
    Agradecemos a sua preferência e confiança!   
==================================================
```

---

## 🚀 Como Usar

### Pré-requisitos
Apenas o **Python 3.8 ou superior** instalado na máquina. Nenhuma biblioteca externa via `pip` é necessária.

### 1. Clonar o Repositório
```bash
git clone https://github.com/s4muelxl/receipt-generator-py.git
cd receipt-generator-py
```

### 2. Executar o Programa

**Opção A — Pelo Terminal:**
```bash
python main.py
```
*(ou `python gerador_recibo.py`)*

**Opção B — No Windows com 1 Clique:**
Dê um duplo clique no arquivo [`executar.bat`](executar.bat). Ele iniciará o programa diretamente no prompt de comando.

---

## 📁 Estrutura do Projeto

```text
receipt-generator-py/
├── .gitignore          # Arquivos e pastas ignoradas pelo Git
├── LICENSE             # Licença MIT de código aberto
├── README.md           # Apresentação e documentação do projeto
├── executar.bat        # Inicializador rápido para Windows
├── gerador_recibo.py   # Lógica principal, validação e formatação
├── main.py             # Ponto de entrada da aplicação
└── recibos/            # Pasta destino onde os comprovantes .txt são salvos
    └── .gitkeep
```

---

## 🛠️ Tecnologias

- **Linguagem:** [Python 3](https://www.python.org/)
- **Módulos Nativos:**
  - `datetime`: Geração de carimbos de data/hora e numeração exclusiva.
  - `os`: Manipulação de diretórios e persistência de arquivos.
  - `sys`: Configuração de encoding UTF-8 no terminal Windows.

---

## 📝 Licença

Este projeto está sob a licença **MIT** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

Desenvolvido por **Samuel Alves**  
- **GitHub:** [@s4muelxl](https://github.com/s4muelxl)

---

<div align="center">
  <sub>Gostou do projeto? Deixe uma ⭐️ no repositório!</sub>
</div>
