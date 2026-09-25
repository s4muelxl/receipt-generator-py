# Gerador de Recibos Automatizado 🧾

Um script simples e eficiente desenvolvido em Python para automatizar a geração de recibos e comprovantes de pedidos de forma rápida via terminal (CLI). 

Este projeto foi desenhado para resolver pequenos gargalos operacionais no dia a dia de vendas, recebendo inputs diretos do usuário e gerando um arquivo `.txt` formatado e pronto para ser compartilhado com o cliente via WhatsApp ou e-mail.

## 🚀 Funcionalidades

- **Input dinâmico:** Inserção de múltiplos produtos, quantidades e valores no mesmo pedido.
- **Cálculo automático:** Subtotais por item e soma automatizada do valor total do pedido.
- **Geração de arquivo:** Exportação imediata para arquivo `.txt` na pasta `recibos/` com formatação limpa, alinhada e profissional.
- **Timestamps e ID único:** Registro automático de data e hora no comprovante gerado e identificador exclusivo do recibo.
- **Pronto para envio:** Formato otimizado para colar e enviar pelo WhatsApp ou e-mail.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x:** Lógica principal e manipulação de arquivos (I/O).
- **Biblioteca `datetime` (Nativa):** Para formatação temporal dos recibos.
- **Biblioteca `os` e `sys` (Nativas):** Sem necessidade de instalar dependências externas (`pip`).

## 📁 Estrutura de Arquivos

```text
recibos_notas/
├── gerador_recibo.py    # Script principal do gerador
├── main.py              # Ponto de entrada do projeto
├── executar.bat         # Atalho para rodar com 2 cliques no Windows
├── README.md            # Documentação do projeto
└── recibos/             # Diretório onde os recibos gerados em .txt são salvos
```

## ⚙️ Como executar o projeto

### Opção 1: Pelo Terminal (PowerShell / Prompt de Comando)

Execute o comando no terminal dentro da pasta do projeto:

```bash
python main.py
```

ou

```bash
python gerador_recibo.py
```

### Opção 2: Com 2 cliques no Windows

Basta clicar duas vezes sobre o arquivo `executar.bat`. Ele detectará o Python instalado e abrirá a tela interativa.

---

## 📄 Exemplo de Recibo Gerado (.txt)

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
    Agradecemos a sua preferência e confiança!   
==================================================
```
