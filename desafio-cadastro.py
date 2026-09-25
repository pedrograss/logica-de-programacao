alunos = []
opcao = ""

while opcao != "4":
    print("\n1-Cadastrar  2-Listar  3-Consultar  4-Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        
      
        nota1 = float(input("Nota 1 (0-10): "))
        while nota1 < 0 or nota1 > 10:
            print("Nota inválida!")
            nota1 = float(input("Digite a Nota 1 novamente: "))

        
        nota2 = float(input("Nota 2 (0-10): "))
        while nota2 < 0 or nota2 > 10:
            print("Nota inválida!")
            nota2 = float(input("Digite a Nota 2 novamente: "))

        
        freq = float(input("Frequência (0-100): "))
        while freq < 0 or freq > 100:
            print("Frequência inválida!")
            freq = float(input("Digite a frequência novamente: "))

        media = (nota1 + nota2) / 2
        
        
        alunos.append([nome, media, freq])
        print("Aluno cadastrado!")

    elif opcao == "2":
        for a in alunos:
            print(f"Aluno: {a[0]}")

    elif opcao == "3":
        for a in alunos:
            nome = a[0]
            media = a[1]
            freq = a[2]
            
            if media >= 7 and freq >= 75: 
                situacao = "Aprovado"
            elif media >= 5 and freq >= 75:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"
                
            print(f"{nome} - Média: {media} - Situação: {situacao}")

