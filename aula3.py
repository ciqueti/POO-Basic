# Herança

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f"O animal {self.nome} está comendo!")

class Cachorro(Animal):
    def latir(self):
        print(f"O cão {self.nome} está latindo: Au Au!!")

class Gato(Animal):
    pass

class Passarinho(Animal):
    pass



# cao = Animal("cão")
cachorro = Cachorro("Adam")

# cao.comer()
cachorro.latir()
cachorro.comer()