agenda = {}       # Diccionario vacío

for _ in range(3):    # Permite agregar 3 contactos
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono            # Clave: nombre, Valor: teléfono

print("Agenda de contactos:")
for nombre, telefono in agenda.items():  # Bucle para recorrer el diccionario
    print(f"{nombre}: {telefono}")
