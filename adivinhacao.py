import random

print("***********************************")
print("Bem-Vindos ao jogo da adivinhação!")
print("***********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("qual nivel de dificuldade?")
print("(1) fácil (2) médio (3) difícil")

nivel = int(input("Escolha o nivel: "))

if(nivel == 1):
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


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
        print("você acertou e fez {} pontos" .format(pontos))
        break
    else:
        if (maior):
            print("você errou, seu chute foi maior que o numero secreto.")
        elif (menor):
            print("você errou, seu chute foi menor que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    #rodada = rodada + 1 (para ser usado com o while para incrementar a variavel)


print("O numero secreto era: " ,numero_secreto)
print("fim do jogo")
