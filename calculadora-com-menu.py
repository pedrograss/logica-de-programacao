print("======= Calculadora Simples ========")
numero = float(input("Digite um número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+ | - | * | /): ")



if operacao == "+":
    soma = numero + numero2
    print(f'A soma é: {soma}')
    
if operacao == "/" and numero2 == 0:
    print(f'Não podemos dividir por zero')
    print("======= Calculadora Simples ========")
    numero = float(input("Digite um número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+ | - | * | /)")

elif operacao == "-":
    subtracao = numero - numero2
    print(f'A subtração é: {subtracao}')

elif operacao == "*":
    multiplicacao = numero * numero2
    print(f'A multiplicação é: {multiplicacao}')

elif operacao == "/":
    divisao = numero / numero2
    print(f'A divisão é: {divisao}')

else:
    print(f'Operação inválida')


 