mochila = []

while True:
    print("1 - Guardar item na mochila: \n2 - Visualizar mochila: \n3 - Ver quantidade de itens: \n4 - Verificar se um item está na mochila: \n5 - Descartar item: \n0 - Sair: ")
     
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja guardar: ")

        if item not in mochila:
            mochila.append(item)
            print(f"{item} foi guardado na mochila!")
        else:
            print(f"{item} já foi guardado anteriormente.")

    elif opcao == "2":
        if len(mochila) == 0:
            print("Sua mochila ainda está vazia.")
        else:
            print("\nItens na mochila:")
            for item in mochila:
                print("-", item)


    elif opcao == "3":
        print(f"Sua mochila possui {len(mochila)} item(ns).")

    elif opcao == "4":
        item = input("Digite o item que deseja procurar: ")

        if item in mochila:
            print(f"{item} foi encontrado na mochila!")

        else:
            print(f"{item} não está na mochila.")

    elif opcao == "5":
        item = input("Digite o item que deseja remover: ")

        if item in mochila:
            mochila.remove(item)
            print(f"{item} foi removido da mochila!")

        else:
            print(f"{item} não foi encontrado na mochila.")

    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break
