from animal import Animal
from model.leon import Leon
from model.aguila import Aguila
from model.paloma import Paloma
from model.gato import Gato
from model.perro import Perro

# 2. ¡IMPORTAMOS EL SERVICIO DE FIREBASE! (CORREGIDO)
from firebase_config import FirebaseRealtime  

try:
    # 3. INICIALIZAMOS LA CONEXIÓN A FIREBASE
    print("Conectando a Firebase...")
    db_service = FirebaseRealtime(base_path="refugio_animal")

    print("\n--- Creando instancias ---")

    aguila1 = Aguila(masa=2.5, especie="águila", voz="kaaauuuuu", edad="1 año")
    leon1 = Leon(masa=80, especie="león", voz="rooar", sexo="macho")
    perro1 = Perro(masa=25, especie="perro", voz="guau guau", raza="pastor alemán")
    gato1 = Gato(masa=3, especie="gato", voz="miaauuu", personalidad="cariñoso")
    paloma1 = Paloma(masa=0.5, especie="paloma", voz="cu curru cu cú", color="gris")

    refugio_animal = [aguila1, leon1, perro1, gato1, paloma1]

    print("\n--- Guardando en Firebase ---")
    for animal in refugio_animal:
        db_service.save_animal(animal)

    # 6. Tu demostración de Polimorfismo (¡perfecto!)
    print("\n--- Demostración de Polimorfismo (Consola) ---")
    for animal in refugio_animal:
        animal.reproducir_voz()
        animal.dormir()

    # --- ¡ERROR 3 CORREGIDO! ---
    # Movimos este bloque para que esté DENTRO del 'try'
    print("\n--- Demostración de Herencia (dormir) ---")
    for animal in refugio_animal:
        animal.dormir()  # <-- Esto funciona gracias al ERROR 2 CORREGIDO

except Exception as e:
    # Capturamos cualquier error (ej. si falla la conexión a Firebase)
    print(f"\n--- ERROR CRÍTICO ---")
    print(f"No se pudo ejecutar el programa: {e}")
    print("Revisa tu 'credentials.json' y la URL en 'firebase_service.py'")
