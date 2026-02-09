def adicionar_produtos(estoque):
    print("ESTOQUE")
    
    nome = input("Digite o nome do produto: ")
    
    if nome in estoque:
        print("Este produto ja existe!")
        return
    
    
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        if quantidade < 0:
            print("Quantidade invalida 2")
            return
    except ValueError:
        print("Quantidade invalida")
        return
    
    
    try:
        preco = float(input("Digite o preco deste produto"))
        if preco <0: 
            print("Preco invalido")
            return
    except ValueError:
        print("Preco invalido")
        return
    
    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print("Produto adicionado com sucesso!")
    
    
    
def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio!")
        return
    
    print("//ESTOQUE//")
    
    soma = 0
    
    for nome, dados in sorted(estoque.items(), key = lambda x: x[0]):
        print(f"{nome}: {dados['quantidade']} unidades - R$ {dados['preco']:.2f} (por unidade)")
        
        soma += dados['quantidade'] *dados['preco']
        
    
    print(f"\nO valor somado de todas as unidades sao: R$ {soma:.2f}")
        
        
def remover_estoque(estoque):
    nome = input("Nome do produto a remover: ")
    
    if nome in estoque:
        del estoque[nome]
        print("produto removido")
    else:
        print("Produto nao encontrado!")
        
        
        
def atualizar_quantidade(estoque):
    nome = input("Nome do produto a alterar quantidade: ")
    
    if nome in estoque:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        estoque [nome] ['quantidade'] = nova_quantidade
        print("Quantidade atualizada! ")
    else: 
        print("Produto nao encontrado! ")
        
        
estoque = {}

while True:
    print("\n=== MENU ===")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade")
    print("5. Sair")
    
    opcao = input("Escolha uma opcao: ")
    
    if opcao == '1':
        adicionar_produtos(estoque)
    elif opcao == '2':
        listar_produtos(estoque)
    elif opcao == '3':
        remover_estoque(estoque)
    elif opcao == '4':
        atualizar_quantidade(estoque)
    elif opcao == '5':
        break
    else:
        print("Opcao invalida.")
        
    
        
    
    
        
    
    
        