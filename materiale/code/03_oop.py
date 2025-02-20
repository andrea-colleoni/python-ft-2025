class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

        
p1 = Persona("Anna", 35)
p2 = Persona("Mario", 28)
p3 = Persona("Luisa", 19)

p1.saluta()
p2.saluta()
p3.saluta()


