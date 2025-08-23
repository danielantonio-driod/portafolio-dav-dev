nombre = input("¿Cómo te llamas? ")             # Cadena
edad = int(input("¿Cuántos años tienes? "))      # Entero
estatura = float(input("Ingresa tu estatura en metros: "))  # Flotante
mayor_edad = edad >= 18                          # Booleano

print("Datos ingresados:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Estatura: {estatura}")
print(f"Mayor de edad: {mayor_edad}")
