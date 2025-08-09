import random
def escolher_palavra():
    palavras = ["python", "programacao", "esclarecedor", "aprendizado", "algoritmo", "escolha", "desafio", "jogo", "forca", "diversao"]
    return random.choice(palavras)

#escolhendo uma palavra do array#
palavra = escolher_palavra()
letras_adivinhadas = ["_"] * len(palavra) #utilizamos a função len para definir o numero de letras da palvra#
letras_tentadas = set() #utilizamos o set para evitar letras repetidas
tentativas = 6 

print("====== Jogo da Forca! =====")

while tentativas > 0 and "_" in letras_adivinhadas:
    print("\nPalavra: ", " ".join(letras_adivinhadas))
    print("letras tentadas: ", ", ".join(sorted(letras_tentadas)))
    print("Tentativas restantes: ", tentativas)

    letra = input("digite uma letra:").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue
    if letra in letras_tentadas:
        print("você ja digitou essa letra, tente novamente.")
        continue
    letras_tentadas.add(letra)
    if letra in palavra:
        print("parabens, voce arcertou a letra!")
        for i, l in enumerate(palavra):
            if l == letra:
                letras_adivinhadas[i] = letra
    else:
        print("você errou a letraae perdeu uma tentativa.")
        tentativas -= 1

#resultado do jogo#
if "_" not in letras_adivinhadas:
    print("\nParabéns! Você adivinhou a palavra:", palavra) 
else:
    print("\nVocê perdeu! A palavra era:", palavra)