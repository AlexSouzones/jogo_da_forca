import os

tentativa = 0
#palavra escolhida para ser adivinhada
palavra = "exemplo"
segredo = len(palavra) * "*"

while True:
    tentativa += 1
    letra = input("Digite uma letra: ")
    tipo = letra.isalpha()
    tamanho = len(letra)

    if tamanho > 1:
        print("Você apenas pode digitar uma letra!")
        continue

    elif tamanho < 1:
        print("Digite ao menos uma letra!")
        continue

    elif not tipo:
        print("Digite um carácter válido!")
        continue

    letra = letra.lower()


    item = 0
    formando = ""
    for p in palavra:
        if segredo[item] != "*":
            formando += segredo[item]
        elif letra == p:
            formando += letra
        else:
            formando +=  "*"

        
        item += 1

    else:
        segredo = formando

    if segredo == palavra:
        os.system("cls")
        print("Parabéns, você acertou!\n"\
              f"A palavra era {palavra}")
        segredo = len(palavra) * "*"
        print(f"Tentativas: {tentativa}")
        tentativa = 0
    else:
        print(segredo)