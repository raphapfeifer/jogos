
def jogar_forca():
    print("********************************")
    print("Bem vindo no jogo de Forca")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?").lower().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        print("jogando...")

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo")

if(__name__== "__main__"):
    jogar_forca()