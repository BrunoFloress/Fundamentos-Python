#
README: Essa aplicação administra uma lista de compras que o usuário irá fazer em um supermercado, 
onde apresentamos ao usuário a possibilidade de adicionar, remover, exibir o carrinho e calcular o toral#



def adicionar_item(carrinho, item, quantidade, preco):
    if item in carrinho:
        carrinho[item]['quantidade'] += quantidade
    else:
        carrinho[item] = {'quantidade': quantidade, 'preco': preco}
def remover_item(carrinho, item):
    if item in carrinho:
        del carrinho[item]
def exibir_carrinho(carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
        return
    print("Itens no carrinho:")
    for item, detalhes in carrinho.items():
        print(f"{item}: {detalhes['quantidade']} unidades a R${detalhes['preco']:.2f} cada")  
def calcular_total(carrinho):
    total = sum(detalhes['quantidade'] * detalhes['preco'] for detalhes in carrinho.values())
    return total
def main():
    carrinho = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Exibir carrinho")
        print("4. Calcular total")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        match escolha:
            case "1":
                item = input("Digite o nome do item: ")
                quantidade = int(input("Digite a quantidade: "))
                preco = float(input("Digite o preço unitário: "))
                adicionar_item(carrinho, item, quantidade, preco)
            case "2":
                item = input("Digite o nome do item a ser removido: ")
                remover_item(carrinho, item)
            case "3":
                exibir_carrinho(carrinho)
            case "4":
                total = calcular_total(carrinho)
                print(f"O total da compra é: R${total:.2f}")
            case "5":
                print("Saindo do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")
if __name__ == "__main__":

    main()
