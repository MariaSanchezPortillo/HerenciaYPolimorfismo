from animal import Animal

class Gato(Animal):
    def __init__(self, masa, especie, voz, personalidad):
        super().__init__(masa, especie, voz)
        self.personalidad = personalidad
        print(f"Su personalidad es: {self.personalidad}.")

        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! Soy un {self.especie} con una personalidad {self.personalidad}.")
