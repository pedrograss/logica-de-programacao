lista = []
pares = 0
impares = 0

for i in range(1, 11):
    numero = float(input("Digite o valor {i}: "))
    lista.append(numero)
    if numero % 2 == 0:
            pares += 1
    elif numero % 2 != 0:
            impares += 1

maior = max(lista)
menor = min(lista)



print(f'Quantidade de pares: {pares}')
print(f'Quantidade de ímpares: {impares}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')


    
