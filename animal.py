#Autor: María José Sánchez Portillo
#Asignación: Polimorfismo y Herencia

class Animal:
    def __init__(self, masa, especie, voz):
        self.masa = masa
        self.especie = especie
        self.voz = voz
        print(f"Creando un {self.especie} de {self.masa} kg.")
        
    def reproducir_voz(self):
        print(f"El sonido que produce el/la {self.especie} es: {self.voz}.")
        
    def dormir(self):
        print(f"El {self.especie} está durmiendo.")
        
        
        
        