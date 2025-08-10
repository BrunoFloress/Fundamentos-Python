temperatura = (float(input("digite a temperatura em Celsius:")))
# Conversor de Temperatura menu
conversao = (input("digite F para farhenheit ou k para Kelvin:")).upper()
match conversao:
    case "F":
        # Fórmula de conversão de Celsius para Fahrenheit
        temperatura_f = (temperatura * 9/5) + 32
        print("A temperadura em Fahrenheit é:", temperatura_f)
    case "K":
        # Fórmula de conversão de Celsius para Kelvin
        temperatura_k = temperatura + 273.15
        print("A temperatura em Kelvin é:", temperatura_k)
    case _:
        print("Opção inválida. Digite 'F' para Fahrenheit ou 'K' para Kelvin.")

