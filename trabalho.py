
mochila = []
#usamos o while true para que o menu continue aparecendo até o usuario decidir sair dele.
while True:
    print("1 - Guardar item na mochila: \n2 - Visualizar mochila: \n3 - Ver quantidade de itens: \n4 - Verificar se um item está na mochila: \n5 - Descartar item: \n0 - Sair: ")
    #fizemos um print único do menu para ficar menor o código ao invés de um print para cada item.
#usamos o input pra receber a oção escolhida pelo usuario (fica armazenado na variavel opção)      
    opcao = input("\nEscolha uma opção: ")
#para cada opcao do menu fizemos um if e elif's com seus respectivos if e else para cada situação, exceto na opção 3 que é somente visualização dos itens da mochila e na opção 0 que é somente para sair.
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
#usamos len para verificar a quantidade de elementos da lista. Se o resultado for zero, significa que a mochila está vazia.

    elif opcao == "3":
        print(f"Sua mochila possui {len(mochila)} item(ns).")

    elif opcao == "4":
        item = input("Digite o item que deseja procurar: ")

        if item in mochila:
            print(f"{item} foi encontrado na mochila!")
# utilizamos if item in mochila para verificar se o item que estamos pedindo existe na lista existe na lista.
        else:
            print(f"{item} não está na mochila.")

    elif opcao == "5":
        item = input("Digite o item que deseja remover: ")

        if item in mochila:
            mochila.remove(item)
            print(f"{item} foi removido da mochila!")
#utilizamos o .remove() para excluir o item que foi informado
        else:
            print(f"{item} não foi encontrado na mochila.")

    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break

    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break
