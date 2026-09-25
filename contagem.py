numero = int(input("Digite um número: "))

contador = 0

for i in range(1, numero + 1):
    if i % 3 == 0:
        print(i)
        contador += 1

print(f'Total de multiplos de 3 encontrados: {contador}')
    

