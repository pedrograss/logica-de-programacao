opcao = ""
while opcao != '3':
    print(f'Menu: ')
    print(f'1 - Cadastrar')
    print(f'2 - Consultar')
    print(f'3 - Sair')

    opcao = input("Escolha uma opção: ")
    opcao = opcao.upper()

    if opcao == "CADASTRAR" or opcao == '1':
        print("Cadastrado")

    elif opcao == "CONSULTAR" or opcao == '2':
        print("Consultado")

    elif opcao == "SAIR" or opcao == '3':
        print("Saindo... ")
        break

    else:
        print(f'Escolha uma das opções informadas')
