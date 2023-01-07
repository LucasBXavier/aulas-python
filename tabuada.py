numero=int (input("Digite um numero a ser multiplicado: "))
print("tabuada do numero: ", numero)
for valor in range (1,11,1):
    print(str(numero) + " x " + str(valor) + " = " + str((numero*valor)))

