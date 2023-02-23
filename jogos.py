import forca
import adivinhacao

def escolhe_jogo():
    print("***********************************")
    print("*********Escolha seu Jogo!*********")
    print("***********************************")

    print("(1) forca (2) adivinhe o numero")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("preparando jogo da forca...")
        forca.jogar_forca()
    elif(jogo == 2):
        print("preparando jogo de adivinhação...")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()