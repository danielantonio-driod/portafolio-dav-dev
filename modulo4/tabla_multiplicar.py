n = int(input("¿Qué tabla quieres ver? "))  # Entero

print(f"Tabla del {n}:")
for i in range(1, 11):                      # Bucle for del 1 al 10
    print(f"{n} x {i} = {n * i}")
