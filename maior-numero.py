maior = int(input("Digite o primeiro número: "))

for i in range(2, 6):
    numero = int(input(f'Digite mais um número: '))

    if numero > maior:
        maior = numero

print(f'O maior número é: {maior}')

            



