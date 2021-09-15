print("********************************")
print("Bem vindo no jogo de adivinhação")
print("********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

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
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu número foi menor do que o número secreto")


print("Fim de jogo")
