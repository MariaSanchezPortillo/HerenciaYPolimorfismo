from animal import Animal

class Paloma(Animal):
    def __init__(self, masa, especie, voz, color):
        super().__init__(masa, especie, voz)
        self.color = color
        print(f"El color es: {self.color}.") 
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! Soy una {self.especie} y mi color es {self.color}.")
