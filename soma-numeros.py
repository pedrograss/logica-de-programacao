numero = int(input("Digite um número: "))

acumulador = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        acumulador += i

print(f'A soma de todos os pares entre 1 e {numero} é: {acumulador}')