lista = [9, 7, 3, 1, 11, 17, 22, 41, 27, 77]

valor = int(input("Digite um número: "))

quantidade = lista.count(valor)

if valor in lista:
    quantidade = lista.count(valor)
    print(f'Está presente e aparece {quantidade} vezes')

else:
    print(f'Esse valor não está na lista')


