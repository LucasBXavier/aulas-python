import PySimpleGUI as gui

print("Olá...")
nome = str(input("Digite seu nome: "))
idade = float(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade")
else:
    print("Maior de idade")

resp = str(input("Gostaria de calcular seu IMC? (s/n)"))

if resp == 's':
    alt = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso atual: "))
