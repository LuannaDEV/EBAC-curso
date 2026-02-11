class Animal:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
        
    def get_name(self):
        return self.name
    
    def get_idade(self):
        return self.idade
        
    def set_nome(self, name):
        self.name = name   
        
    def set_idade(self, idade):
        self.idade = idade
        
        
        
    def emitir_som(self):
        pass
    
    
        

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu")
        
                
class Gato(Animal):
    def emitir_som(self):
        print("O gato miou")
        
        
        
        


gato = Gato("Tom", 3)
cachorro = Cachorro("Max", 5)

gato.emitir_som()
cachorro.emitir_som()


gato.set_idade(4)
cachorro.set_idade(6)