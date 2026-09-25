nota = float(input("Digite a nota para saber a situação atual do aluno: "))

if nota >= 7:
    print(f'Aprovado, nota do aluno: {nota}')

elif nota >= 5:
    print(f'Recuperação, nota do aluno: {nota}')

else:
    print(f'Reprovado, possui a nota: {nota}')