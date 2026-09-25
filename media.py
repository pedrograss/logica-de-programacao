quantidade = int(input("Digite a quantidade de alunos: "))

aprovados = 0
for aluno in range(quantidade):
    nota1 = float(input("Digite a nota 1:"))
    nota2 = float(input("Digite a nota 2:"))
    nota3 = float(input("Digite a nota 3:"))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado")
        aprovados += 1
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

print(f'Alunos aprovados foram: {aprovados}')

    

