class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print(f"O animal {self.nome} emitiu um som genérico")
    
class Cachorro(Animal):
    def emitir_som(self):
        print(f"O cachorro {self.nome} latiu")

class Gato(Animal):
    def emitir_som(self):
        print(f"O gato {self.nome} miou")

cao = Cachorro("Adam", 22)
gato = Gato("Little_Cat", 5)

cao.emitir_som()
gato.emitir_som()