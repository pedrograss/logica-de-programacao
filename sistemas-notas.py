
quantidade_alunos = int(input("Digite a quantidade de alunos: "))

notas = []

for i in range(1, quantidade_alunos + 1):
    while True:
        nota = float(input(f"Digite a nota do aluno {i} (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida! A nota deve estar entre 0 e 10. Tente novamente.")


media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)


aprovados = 0
for nota in notas:
    if nota >= 7.0:
        aprovados += 1


print("\n--- RESUMO DA TURMA ---")
print(f"Lista de notas: {notas}")
print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Quantidade de notas >= 7: {aprovados}")