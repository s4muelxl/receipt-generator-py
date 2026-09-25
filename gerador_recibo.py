import os
import sys
from datetime import datetime

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def converter_para_float(valor_str: str) -> float:
    limpo = valor_str.replace("R$", "").replace("r$", "").strip()
    if "." in limpo and "," in limpo:
        limpo = limpo.replace(".", "").replace(",", ".")
    elif "," in limpo:
        limpo = limpo.replace(",", ".")
    return float(limpo)

def limpar_nome_arquivo(texto: str) -> str:
    caracteres_invalidos = '<>:"/\\|?* '
    limpo = "".join(c if c not in caracteres_invalidos else "_" for c in texto)
    return limpo.strip("_") or "cliente"

def obter_input_float(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip()
        try:
            val = converter_para_float(entrada)
            if val < 0:
                print(">> [AVISO] O valor não pode ser negativo. Tente novamente.")
                continue
            return val
        except ValueError:
            print(">> [AVISO] Valor inválido! Digite um número válido (ex: 29.90 ou 29,90).")

def obter_input_qtd(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            return 1.0
        try:
            qtd = converter_para_float(entrada)
            if qtd <= 0:
                print(">> [AVISO] A quantidade deve ser maior que zero.")
                continue
            return qtd
        except ValueError:
            print(">> [AVISO] Quantidade inválida! Digite um número (ex: 1, 2, 0.5).")

def gerar_recibo():
    print("\n" + "=" * 52)
    print("           GERADOR DE RECIBOS AUTOMATIZADO          ")
    print("=" * 52)

    cliente = input("\nNome do Cliente: ").strip()
    if not cliente:
        cliente = "Consumidor Final"

    contato = input("Telefone / Contato (opcional): ").strip()
    forma_pagamento = input("Forma de Pagamento (ex: Pix, Dinheiro, Cartao): ").strip()
    if not forma_pagamento:
        forma_pagamento = "Nao informada"

    itens = []
    print("\n--- Inserção de Itens / Produtos ---")
    print("(Dica: Pressione ENTER com o nome vazio para finalizar)")

    contador = 1
    while True:
        print(f"\nItem #{contador}:")
        nome_produto = input("  Nome do produto/serviço: ").strip()
        if not nome_produto:
            if not itens:
                print(">> [AVISO] Adicione pelo menos um item ao recibo!")
                continue
            break

        quantidade = obter_input_qtd("  Quantidade [Padrão: 1]: ")
        valor_unitario = obter_input_float("  Valor Unitário (R$): ")
        subtotal = quantidade * valor_unitario

        itens.append({
            "nome": nome_produto,
            "quantidade": quantidade,
            "valor_unitario": valor_unitario,
            "subtotal": subtotal
        })
        contador += 1

        opcao = input("\nAdicionar mais um item? (S/N) [S]: ").strip().lower()
        if opcao in ["n", "nao", "não"]:
            break

    observacao = input("\nObservações adicionais (opcional): ").strip()

    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y às %H:%M:%S")
    id_recibo = agora.strftime("%Y%m%d-%H%M%S")
    valor_total = sum(item["subtotal"] for item in itens)

    linhas = []
    linhas.append("=" * 50)
    linhas.append("         COMPROVANTE / RECIBO DE PEDIDO         ")
    linhas.append("=" * 50)
    linhas.append(f"Data/Hora : {data_formatada}")
    linhas.append(f"Recibo Nº : #{id_recibo}")
    linhas.append(f"Cliente   : {cliente}")
    if contato:
        linhas.append(f"Contato   : {contato}")
    linhas.append(f"Pagamento : {forma_pagamento}")
    linhas.append("-" * 50)
    linhas.append(f"{'QTD':<5} {'DESCRIÇÃO':<28} {'TOTAL':>15}")
    linhas.append("-" * 50)

    for item in itens:
        qtd_str = f"{int(item['quantidade'])}x" if item['quantidade'].is_integer() else f"{item['quantidade']}x"
        nome = item["nome"]
        total_item_str = formatar_moeda(item["subtotal"])
        
        if len(nome) > 28:
            nome_linha = nome[:25] + "..."
        else:
            nome_linha = nome

        linhas.append(f"{qtd_str:<5} {nome_linha:<28} {total_item_str:>15}")
        
        if item["quantidade"] != 1:
            detalhe = f"     ({qtd_str} de {formatar_moeda(item['valor_unitario'])})"
            linhas.append(detalhe)

    linhas.append("-" * 50)
    total_str = formatar_moeda(valor_total)
    linhas.append(f"{'VALOR TOTAL:':<30} {total_str:>19}")
    linhas.append("-" * 50)

    if observacao:
        linhas.append(f"Observações: {observacao}")
        linhas.append("-" * 50)

    linhas.append("    Agradecemos a sua preferência e confiança!   ")
    linhas.append("=" * 50)

    conteudo_recibo = "\n".join(linhas)

    pasta_destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recibos")
    os.makedirs(pasta_destino, exist_ok=True)

    nome_arquivo = f"recibo_{limpar_nome_arquivo(cliente)}_{id_recibo}.txt"
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo_recibo)

    print("\n" + "=" * 50)
    print("             RECIBO GERADO COM SUCESSO!           ")
    print("=" * 50 + "\n")
    print(conteudo_recibo)
    print("\n" + "-" * 50)
    print(f"[ARQUIVO SALVO]:\n{caminho_arquivo}")
    print("-" * 50)

def main():
    try:
        while True:
            gerar_recibo()
            print("\n" + "=" * 52)
            continuar = input("Deseja gerar outro recibo? (S/N) [N]: ").strip().lower()
            if continuar not in ["s", "sim"]:
                print("\nEncerrando o gerador de recibos. Até a próxima!\n")
                break
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário. Até logo!\n")

if __name__ == "__main__":
    main()
