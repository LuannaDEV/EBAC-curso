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
        tipo = input("Qual o tipo do pokemon? ")
        
        while True:
            nivel = int(input("Qual o nivel do pokemon? "))
            if nivel > 100 or nivel <= 0:
                print("valor invalido! Nivel tem que ser maior que 0 e menor que 100")
            else:
                break   
            
        
        
        
        novo_pokemon = {
            "nome": nome,
            "tipo": tipo,
            "nivel": nivel
        }

        pokemon.append(novo_pokemon)
        print(f"Pokemon {nome} adicionado com sucesso!")

    except ValueError:
        print("Valor inválido! O nível deve ser um número.")
        
        
def atualizar():
    try:
        pokemon_nome = input("Qual pokemon voce deseja remover?")
        
        for p in pokemon:
            if p["nome"].lower() == pokemon_nome.lower():
                p["tipo"] = input("Novo tipo:")
                p["nivel"] = int(input("Novo nivel:"))
                print("Pokemon atualizado!")
                return
        print("Este pokemon nao existe")
    except ValueError:
        print("Valor invalido!")
        

def deletar():
    try:
        pokemon_nome = input("Qual pokemon voce deseja deletar: ")
        
        for p in pokemon:
            if p["nome"].lower() == pokemon_nome.lower():
                pokemon.remove(p)4
                print("pokemon deletado com sucesso")
                return
            print("Este pokemon nao existe!")
    except ValueError:
        print("valor invalido!")            
        
        
def listar():
    if not pokemon:
        print("nao ha nenhum pokemon!")
        return
    for p in pokemon:
        print(f"Nome: {p['nome']} | Tipo: {p['tipo']} | Nivel: {p['nivel']} | Capturas: {p['capturas']}")
   
   

        
def capturas():
    if not pokemon:
        print("nao ha nenhum pokemon!")
        return
    pokemon_escolhido = input("Digite o pokemon que deseja atualizar: ")  
    
    encontrado = False
    
    for p in pokemon:
        if p["nome"].lower() == pokemon_escolhido:
            quant = int(input("Digite a quantidade de vezes que ele foi capturado: "))
            p["capturas"] = quant
            print("Quantidade de capturas do pokemon atualizada!")
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
        
       
            
def exibir_historico():
    if not historico_capturas:
        print("Nao existe nenhum historico de captura!")
        return
    
    for p in historico_capturas:
        
        print(f"Nome: {p['nome']} | Capturas:  {p['capturas']}")
      
    

    
def main():
    while True:
        menu()

        try:
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                adicionar()
            if opcao == "2":
                atualizar()
            if opcao == "3":
                deletar()
            if opcao == "4":
                listar()
            if opcao == "5":
                capturas()
            if opcao == "6":
                exibir_historico()
            if opcao == "7":
                break
            
        except ValueError:
            print("valor invalido!")
        
 
main()