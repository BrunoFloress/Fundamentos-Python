import random
import string
import secrets

def GerarSenha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True, excluir_ambiguidades=False):
    if tamanho > 50:
        raise ValueError("O tamanho máximo da senha é 50 caracteres.")
    if tamanho < 5:
        raise ValueError("O tamanho mínimo da senha é 5 caracteres.")

    # definição dos caracteres que serão usados na senha
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%¬&*()`}{^?:><,.;/?]~[]"

    ambiguos = "il1Lo0O"
    if excluir_ambiguidades:
        maiusculas = ''.join(c for c in maiusculas if c not in ambiguos)
        minusculas = ''.join(c for c in minusculas if c not in ambiguos)
        numeros = ''.join(c for c in numeros if c not in ambiguos)
        simbolos = ''.join(c for c in simbolos if c not in ambiguos)

    caracteres = []
    caracteres_usados = []

    if usar_maiusculas:
        caracteres.append(maiusculas)
        caracteres_usados.append(secrets.choice(maiusculas))
    if usar_minusculas:
        caracteres.append(minusculas)
        caracteres_usados.append(secrets.choice(minusculas))
    if usar_numeros:
        caracteres.append(numeros)
        caracteres_usados.append(secrets.choice(numeros))
    if usar_simbolos:
        caracteres.append(simbolos)
        caracteres_usados.append(secrets.choice(simbolos))

    # junta todos os caracteres disponíveis
    todos_caracteres = ''.join(caracteres)

    # gera o restante da senha
    senha = "".join(secrets.choice(todos_caracteres) for _ in range(tamanho - len(caracteres_usados)))

    # adiciona os caracteres obrigatórios
    senha += ''.join(caracteres_usados)

    # embaralha a senha
    senha = ''.join(random.sample(senha, len(senha)))
    return senha

def main():
    tamanho = int(input("Digite quantos caracteres a senha deve ter (5 a 50): "))
    usar_maiusculas = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Usar letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Usar números? (s/n): ").lower() == 's'
    usar_simbolos = input("Usar símbolos? (s/n): ").lower() == 's'
    excluir_ambiguidades = input("Excluir caracteres ambíguos? (s/n): ").lower() == 's'

    for _ in range(6):
        senha = GerarSenha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos, excluir_ambiguidades)
        print("Senha gerada:", senha)

if __name__ == "__main__":
    main()
