'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''


def calcular_total_carrinho():
    """Cria um carrinho de compras e calcula o total."""

    carrinho = {}  # Dicionário para armazenar produtos e quantidades

    # Adiciona produtos ao carrinho
   
    while True:
        produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")
        if produto == "fim":
            break
        while True:  # Loop para garantir entrada válida
            try:
                quantidade = int(input("Digite a quantidade: "))
                if quantidade > 0:
                    carrinho[produto] = quantidade
                    break
                else:
                    print("Quantidade inválida. Digite um valor maior que zero.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    total = sum(carrinho.values())  # Soma as quantidades dos produtos
    print("Total do carrinho de compras:", total)

calcular_total_carrinho()