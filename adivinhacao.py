print("********************************")
print("Bem vindo no jogo de adivinhação")
print("********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa", rodada, "de", total_tentativas)
    chute = input("Digite o seu número: ")

    print("Você digitou: ", chute)

    acertou = numero_secreto == int(chute)
    maior = int(chute) > numero_secreto
    menor = int(chute) < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu número foi menor do que o número secreto")

    rodada = rodada +1

print("Fim de jogo")
