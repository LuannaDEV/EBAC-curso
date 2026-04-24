pokemon = []  
historico_capturas = []   

def menu():
    print("// menu //")
    print("1 - adicionar pokemon")
    print("2 - atualizar pokemon")
    print("3 - remover pokemon")
    print("4 - listar pokemons")
    print("5 - atualizar a quantidade de capturas")
    print ("6 - exibir o historico de capturas")
    print("7 - sair do programa")

def adicionar():
    try:
        nome = input("Qual o nome do pokemon? ")
        
        for p in pokemon:
            if p["nome"].lower() == nome.lower():
                print("Este pokemon ja existe!")
                return
        
        tipo = input("Qual o tipo do pokemon? ")
        capturas = int(input("Quantas vezes voce capturou este pokemon? "))
        

        nivel = int(input("Qual o nivel do pokemon? "))
        if nivel > 100 or nivel <= 0:
            print("valor invalido! Nivel tem que ser maior que 0 e menor que 100")
            return
        
                
            
        novo_pokemon = {
            "nome": nome,
            "tipo": tipo,
            "nivel": nivel,
            "capturas":capturas
        }

        pokemon.append(novo_pokemon)
        print(f"Pokemon {nome} adicionado com sucesso!")

    except ValueError:
        print("Valor inválido! O nível deve ser um número.")
        
        
def atualizar():
    if not pokemon:
        print("Nao ha nenhum pokemon!")  
        return
    try:
        pokemon_nome = input("Qual pokemon voce deseja atualizar?")
        
        for p in pokemon:
            if p["nome"].lower() == pokemon_nome.lower():
                
                novo_tipo = input("Novo tipo: ")
                novo_nivel = int(input("Novo nivel: "))

                
                if novo_nivel >100 or novo_nivel <=0:
                    print("Valor invalido! Nivel tem que ser maior que 0 e menor ou igual a 100.")
                    return
                p["tipo"] = novo_tipo
                p["nivel"] = novo_nivel
                print("Pokemon atualizado")
                return
                     
       
        print("Este pokemon nao existe")
    except ValueError:
        print("Valor invalido!")
            

def deletar():
    try:
        pokemon_nome = input("Qual pokemon voce deseja deletar? ")
        
        for p in pokemon:
            if p["nome"].lower() == pokemon_nome.lower():
                pokemon.remove(p)
                print(f"O pokemon {pokemon_nome} foi deletado com sucesso!")
                return
        print("Este pokemon nao existe na lista!")
    except ValueError:
        print("valor invalido! Tente novamente.")            
        
        


        
def capturas():
    if not pokemon:
        print("nao ha nenhum pokemon!")
        return
    pokemon_escolhido = input("Digite o pokemon que deseja atualizar: ")  
        
    encontrado = False
        
    for p in pokemon:
        if p["nome"].lower() == pokemon_escolhido.lower():
            quant = int(input("Digite a quantidade de vezes que ele foi capturado: "))
            p["capturas"] = quant
            print(f"Quantidade de capturas do pokemon {pokemon_escolhido} atualizada para {quant}")
            encontrado = True
                

            entrada = {
                "nome":p["nome"],
                "capturas": quant 
            }
            historico_capturas.append(entrada)
            print(f"Capturas de {p['nome']} atualizadas para {quant}!")
            
            
            break
                
    if not encontrado:
        print("Este pokemon nao existe!")
        
       
def listar():
    if not pokemon:
        print("nao ha nenhum pokemon na lista!")
        return
    for p in pokemon:
        print(f"Nome: {p['nome']} | Tipo: {p['tipo']} | Nivel: {p['nivel']} | Capturas: {p['capturas']}")
   
          
       
       

       
       
       
            
def exibir_historico():
    if not historico_capturas:
        print("Nao existe nenhum historico de captura!")
        return
    
    for p in historico_capturas:
        print("//HISTORICO CAPTURA POKEMONS//")
       
        print(f"Nome: {p['nome']} | Capturas:  {p['capturas']}")
      
    

    
def main():
    while True:
        menu()

        try:
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                adicionar()
            elif opcao == "2":
                atualizar()
            elif opcao == "3":
                deletar()
            elif opcao == "4":
                listar()
            elif opcao == "5":
                capturas()
            elif opcao == "6":
                exibir_historico()
            elif opcao == "7":
                break
            
        except ValueError:
            print("valor invalido! Escolha uma opcao dentro da lista.")
        
 
main()