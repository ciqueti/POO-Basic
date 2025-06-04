# Seguem os Atributos
# Nome
# HP
# Tipo do Pokemon (Terra, Água, Fogo)
# Ataques (choque do trovão)
# Altura
# Peso

# Pikachu
# HP -> 300
# Tipo -> Elétrico
# Ataque -> Choque do trovão
# Altura - 15cm
# Peso - 15kg

# Charizard
# HP -> 450
# Tipo -> Fogo
# Ataque -> Lança Chamas
# Altura -> 2m
# Peso -> 200kg

class MoldePokemon:
    # Método ou Função construtor 
    # Self tem a responsibilidade de armazenar e manipular as informações dos atributos
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso
        
    def mostrar_nome_pokemon(self):
        print(f"O nome do pokemon eh {self.nome}")

    def mostrar_altura_pokemon(self):
        print(f"A Altura do pokemon eh {self.altura}")

# Criando objetos, a partir da classe (Molde)

pikachu = MoldePokemon("Pikachu", 15, "Elétrico", "choque do trovão", 15, 10)
charizard = MoldePokemon("Charizard", 20, "Fogo", "bola de fogo", 175, 200)
miau = MoldePokemon("Miau", 20, "Terrestre", "Garra", 13, 10)

# O objeto pikachu da classe MoldePokemon possui o método mostrar_nome_pokemon()
pikachu.mostrar_nome_pokemon()
charizard.mostrar_nome_pokemon()
miau.mostrar_altura_pokemon()