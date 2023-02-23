print("******************")
print("adivinhe o numero!")
print("******************")

num_secreto = 19
tentativa = 3
rodada = 1

while(rodada <= tentativa):
    print("\n")
    chute = int(input("escreva seu numero: "))

    acertou = chute == num_secreto
    maior   = chute > num_secreto
    menor   = chute < num_secreto

    print("Você digitou: ", chute)

    if acertou:
        print("Você acertou")
    else:
        if maior:
            print("errou, você digitou um numero maior")
        elif menor:
            print("errou, você digitou um numero menor")

    rodada = rodada + 1

print("Fim do jogo")