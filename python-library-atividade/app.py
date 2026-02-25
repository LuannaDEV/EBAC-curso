def menu():
    
    print("///MENU///")
    
    print("1 - Para escolher adicionar livros")
    
    print("2 - Para escolher remover livros")
    
    print("3 - Para escolher listar todos os livros")
   
    print("4 - Para escolher atualizarr a quantidade de livros")
    
    print("5 - Para escolher registar um emprestimo")
   
    print("6 - Exibir historico de emprestimos")
    
    print("7 - Finalizar o programa")
    
    
    
def adicionar_livro(biblioteca):
    titulo = input("Qual o titulo do livro ")
    autor = input("Qual o nome do autor ")
    quantidade = int(input("Quantos livros? "))
    
    biblioteca[titulo] = {"autor": autor, "quantidade": quantidade}
    
    
    

def remover_livro(biblioteca):
    escolha = input("Qual livro voce deseja escolher? ")
        
    if escolha not in biblioteca:
        print("Este livro nao existe.")
        return
    
    
    del biblioteca[escolha]
    print(f'Livro "{escolha}" removido com sucesso!')
    
    
def listar_livros(biblioteca):
    if not biblioteca:
        print("A biblioteca esta vazia!")
        return

    for titulo,info in biblioteca.items():
        print (f'Titulo: {titulo} / Autor: {info["autor"]} / {info["quantidade"]}')
        
        
def atualizar_quantidade(biblioteca):
    titulo =  input("Qual livro deseja atualizar a quantidade? ")
    
    if livro not in biblioteca: 
        print("Este livros nao esta na biblioteca!")
        return
    
    nova_quantidade = int(input(f'Qual a nova quantidade? Quantidade atual:  {biblioteca[titulo] ["quantidade"]} Quantidade atual: '))
    biblioteca[titulo]["quantidade"] = nova_quantidade
    
    print(f'Quantidade atualizar do livro:{titulo}   para:  {novaquantidade}')
    
    
    
    def fazer_emprestimo(biblioteca,historico):
        titulo = input("Qual o titulo do livro para emprestimo? ")


        if titulo not in biblioteca:
            print("Este livro nao existe")
            return
        
        if biblioteca[titulo]["quantidade"] == 0:
            print("Nao ha quantidade disponivel deste livro.")
            return
        nome = input("Digite o nome do solicitante")
        biblioteca[titulo]["quantidade"] -=1
        historico.append({"livro": titulo, "solicitante": nome})
        print(f'Emprestimo de "{titulo}" registrado para {nome}!')
        
        
    def exibir_historico( historico):
        if not historico:
            print("Nao exite historico de emprestimos.")
            return
        
        print("\n--- Historico de Emprestimos ---")
        
        for i, registro in enumerate(historico, 1):
            print(f'{i}. Livro: {registro["livro"]} / Solicitante: {registro["solicitante"]}')

        
def main():
    historico = []
    biblioteca = {}
   
    while True:
        
        
        menu()
        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            adicionar_livro(biblioteca)
        elif opcao == "2":
            remover_livro(biblioteca)
        elif opcao == "3":
            listar_livros(biblioteca)
        elif opcao == "4":
            atualizar_quantidade(biblioteca)
        elif opcao == "5":
            registrar_livro(biblioteca, historico)
        elif opcao == "6":
            exibir_historico(historico)
        elif opcao == "7":
            print("Encerrando o programa. Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")
            
main()          
    

        
         