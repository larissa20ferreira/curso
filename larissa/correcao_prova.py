"""estoque = {}
while True:
    print("Sistema de gerenciamento de estoque")
    print("1- Adicionar novos produtos")
    print("2- Atualize a quantidade de produtos")
    print("3- Remover produtos")
    print("4- Exibir o estoque")
    print("5- Buscar um produto")
    print("6- Sair")
    print("=======================================")
    opcao = int(input("Escolha uma opção:"))
    if opcao == 1:
        nome = input("Nome do produto: ")
        quantidade = int(input("Informe a quantidade:"))
        preco = float(input("Informe o preço:"))
        if nome in estoque:
            print("Produto já existe no estoque...")
        else:
            estoque[nome] = {'Quantidade': quantidade, 'preco' : preco}
    elif opcao == 2:
        nome = input("Nome do produto a ser atualizado: ")
        if nome in estoque:
            quantidade = int(input("Informe a nova quantidade: "))
            estoque[nome]['Quantidade'] = quantidade
        else:
            print("Produto não encontrado!")
    elif opcao == 3:
        print("Nome do produto removido:")
        if nome in estoque:
            del estoque[nome]
        else:
            print("Produto não encontrado!")
    elif opcao == 4:
        if estoque:
            print("Estoque atual: ")
            for nome, detalhes in  estoque.items():
                print(f"Produto: {nome}, Quantidade{detalhes['Quantidade']}, preço{detalhes['preco']}")
        else:
            print("Estoque vazio.")
    elif opcao == 5:
        nome = input("Nome do produto a ser buscado: ")
        if nome in estoque:
            detalhes = estoque[nome]
            print(f"Produto: {nome}, Quantidade{detalhes['Quantidade']}, Preço{detalhes['preco']}")
        else:
            print("Produto não encontrado!")
    elif opcao == 6:
        print("Saindo do sistema")
    else:
        print("Opção inválida. Tente novamente:")"""