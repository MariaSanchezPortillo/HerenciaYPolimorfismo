from animal import Animal

class Aguila(Animal):
    def __init__(self, masa, especie, voz, edad):
        super().__init__(masa, especie, voz)
        self.edad = edad  
        print(f"La edad que tiene es: {self.edad}.")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! Soy un {self.especie} y tengo {self.edad} años.")
