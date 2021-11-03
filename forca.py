import random





def jogar_forca():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = incializa_palavras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        print("jogando...")

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()




def imprime_mensagem_abertura():
    print("********************************")
    print("Bem vindo no jogo de Forca")
    print("********************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero]
    return palavra_secreta

def incializa_palavras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?").lower().strip()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")

if(__name__== "__main__"):
    jogar_forca()