n1 = 0.0
n2 = 0.0

soma = 0.0
subtracao = 0.0
multiplicacao = 0.0 
divisao = 0.0

#operacoes#
def CalcularOperacoes(n1, n2):
    global soma, subtracao, multiplicacao, divisao
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2 if n2 != 0 else "Erro: Divisão por zero"
    return soma, subtracao, multiplicacao, divisao

while True:
    #input dos numeros#
    print("insira o primeiro numero: ")
    n1 = float(input())
    print("insira o segundo numero: ")
    n2 = float(input())  
    
    #Menu da Calculadora#
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = input("Digite o número da operação: ")

    match escolha:
        case "1":
            print("Soma: ", n1 + n2)
        case "2":
            print("Subtração:", n1 - n2)
        case "3":
            print("Multiplicação: ", n1 * n2)
        case "4":
            if n2 != 0:
                print("Divisão: ", n1 / n2)
            else:
                print("Erro: Divisão por zero")
        case "5":
            print("Encerrando a calculadora...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
