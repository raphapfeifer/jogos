import random
def jogar_adivinhacao():
    print("********************************")
    print("Bem vindo no jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for rodada in range(1, total_tentativas + 1) :
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite um número entre 1 e 100: ")

        print("Você digitou: ", chute)

        if (int(chute) < 1 or int(chute) > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == int(chute)
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu número foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - int(chute))
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__=="__main__"):
    jogar_adivinhacao()