list = []

for i in range(1, 6):
    nome = input(f"Digite o {i}º nome: ")
    list.append(nome)

print("\n--- Nomes Cadastrados ---")
for nome in list:
    print(f"- {nome}")

