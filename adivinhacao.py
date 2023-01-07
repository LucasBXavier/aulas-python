print("***********************************")
print("Bem-Vindos ao jogo da adivinhação!")
print("***********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

#while (rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    print("\n")
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um numero entre 1 e 100: "))

    print("\n")
    print("Você digitou: ", chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue


    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if (acertou):
        print("você acertou")
        break
    else:
        if (maior):
            print("você errou, seu chute foi maior que o numero secreto.")
        elif (menor):
            print("você errou, seu chute foi menor que o numero secreto.")

    #rodada = rodada + 1 (para ser usado com o while para incrementar a variavel)

print("fim do jogo")
