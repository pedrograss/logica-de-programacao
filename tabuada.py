numero = int(input("Digite um número para saber a sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, " x ", i, " = ", resultado)