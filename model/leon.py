from animal import Animal

class Leon(Animal):
    def __init__(self, masa, especie, voz, sexo):
        super().__init__(masa, especie, voz)
        self.sexo = sexo 
        print(f"Su sexo es: {self.sexo}.")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! Soy un {self.especie} {self.sexo}.")
