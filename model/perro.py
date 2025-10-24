from animal import Animal

class Perro(Animal):
    def __init__(self, masa, especie, voz, raza):
        super().__init__(masa, especie, voz)
        self.raza = raza
        print(f"Su raza es: {self.raza}")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! Soy un {self.especie} de raza {self.raza}.")
