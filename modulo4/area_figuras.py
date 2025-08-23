def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    import math
    return math.pi * radio ** 2

print("Elige la figura:")
print("1) Rectángulo")
print("2) Círculo")
op = input("Opción: ")

if op == "1":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print(f"Área: {area_rectangulo(base, altura)}")
elif op == "2":
    radio = float(input("Radio: "))
    print(f"Área: {area_circulo(radio)}")
else:
    print("Opción no válida.")
