"""
portafolio_mod3.py
Autor: Daniel Arrieta (bootcamp Python) — Entrega Módulo 3

Este script de consola reúne ejercicios cortos que demuestran:
1) Variables, operadores y tipos básicos (str, int, float, bool).
2) Condicionales if/elif/else.
3) Bucles for y while.
4) Estructuras de datos (listas, tuplas, diccionarios).
5) Funciones para modularizar y reutilizar código.
6) Un menú simple que organiza todo.

Uso:
    python portafolio_mod3.py

Nota:
    No requiere archivos externos ni librerías de terceros.
"""

# ----------------------------- Utilidades de entrada -----------------------------

def leer_int(prompt: str) -> int:
    """Lee un entero desde consola, reintentando si hay error."""
    while True:
        valor = input(prompt).strip()
        if valor.lstrip("-").isdigit():  # permite números negativos
            return int(valor)
        print("⚠️  Por favor ingresa un número entero válido.")


def leer_float(prompt: str) -> float:
    """Lee un float desde consola, reintentando si hay error."""
    while True:
        valor = input(prompt).strip().replace(",", ".")  # acepta coma o punto
        try:
            return float(valor)
        except ValueError:
            print("⚠️  Ingresa un número (puede llevar decimales).")


def leer_bool(prompt: str) -> bool:
    """Lee un booleano 's/n' o 'si/no' y devuelve True/False."""
    while True:
        valor = input(prompt + " [s/n]: ").strip().lower()
        if valor in ("s", "si", "sí"):
            return True
        if valor in ("n", "no"):
            return False
        print("⚠️  Responde con 's' o 'n'.")


# ----------------------------- 1) Conversor de unidades -----------------------------

def conversor_unidades():
    """
    Demuestra:
    - variables y operadores
    - tipos numéricos
    - condicionales y menús
    """
    while True:
        print("\n=== Conversor de Unidades ===")
        print("1) Temperatura (°C ↔ °F ↔ K)")
        print("2) Monedas (CLP ↔ USD) *tasa fija de ejemplo")
        print("3) Longitud (m ↔ km ↔ millas)")
        print("0) Volver")
        op = leer_int("Elige opción: ")

        if op == 0:
            return

        elif op == 1:
            print("\n-- Temperatura --")
            print("1) °C a °F | 2) °F a °C | 3) °C a K | 4) K a °C")
            t = leer_int("Elige conversión: ")
            v = leer_float("Ingresa el valor: ")

            if t == 1:
                res = (v * 9/5) + 32
                print(f"{v} °C = {res:.2f} °F")
            elif t == 2:
                res = (v - 32) * 5/9
                print(f"{v} °F = {res:.2f} °C")
            elif t == 3:
                res = v + 273.15
                print(f"{v} °C = {res:.2f} K")
            elif t == 4:
                res = v - 273.15
                print(f"{v} K = {res:.2f} °C")
            else:
                print("Opción inválida.")

        elif op == 2:
            print("\n-- Monedas -- (Tasas de ejemplo, fijas)")
            # Variables "constantes" para el ejemplo
            CLP_POR_USD = 900.0   # 1 USD ≈ 900 CLP (ejemplo estático)
            print("1) CLP a USD | 2) USD a CLP")
            t = leer_int("Elige conversión: ")
            v = leer_float("Ingresa el monto: ")

            if t == 1:
                res = v / CLP_POR_USD
                print(f"${v:,.0f} CLP ≈ ${res:,.2f} USD")
            elif t == 2:
                res = v * CLP_POR_USD
                print(f"${v:,.2f} USD ≈ ${res:,.0f} CLP")
            else:
                print("Opción inválida.")

        elif op == 3:
            print("\n-- Longitud --")
            print("1) m a km | 2) km a m | 3) km a millas | 4) millas a km")
            t = leer_int("Elige conversión: ")
            v = leer_float("Ingresa el valor: ")
            if t == 1:
                print(f"{v} m = {v/1000:.3f} km")
            elif t == 2:
                print(f"{v} km = {v*1000:.0f} m")
            elif t == 3:
                print(f"{v} km = {v*0.621371:.3f} millas")
            elif t == 4:
                print(f"{v} millas = {v/0.621371:.3f} km")
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida.")


# ----------------------------- 2) Formulario (tipos de datos) -----------------------------

def formulario_usuario():
    """
    Pide datos al usuario y los almacena en variables con tipos adecuados,
    demostrando str, int, float y bool.
    """
    print("\n=== Formulario de Usuario ===")
    nombre = input("Nombre: ").strip()                  # str
    edad = leer_int("Edad (años): ")                    # int
    estatura = leer_float("Estatura (metros): ")        # float
    suscrito = leer_bool("¿Deseas recibir novedades por correo?")  # bool

    print("\nResumen de datos y tipos:")
    print(f"Nombre: {nombre!r} -> {type(nombre).__name__}")
    print(f"Edad: {edad} -> {type(edad).__name__}")
    print(f"Estatura: {estatura} -> {type(estatura).__name__}")
    print(f"Suscrito: {suscrito} -> {type(suscrito).__name__}")


# ----------------------------- 3) Condicional simple -----------------------------

def signo_de_numero():
    """Determina si un número es positivo, negativo o cero (if/elif/else)."""
    print("\n=== Signo de un número ===")
    n = leer_float("Ingresa un número: ")
    if n > 0:
        print("El número es POSITIVO.")
    elif n < 0:
        print("El número es NEGATIVO.")
    else:
        print("El número es CERO.")


# ----------------------------- 4) Iteraciones (for/while) -----------------------------

def tablas_o_factorial():
    """
    Submenú que demuestra bucles:
    - for: genera tabla de multiplicar
    - while: calcula factorial
    """
    while True:
        print("\n=== Iteraciones ===")
        print("1) Tabla de multiplicar (for)")
        print("2) Factorial (while)")
        print("0) Volver")
        op = leer_int("Elige opción: ")
        if op == 0:
            return

        if op == 1:
            base = leer_int("¿Tabla de qué número? ")
            hasta = leer_int("¿Hasta qué multiplicador? (p.ej. 10) ")
            print(f"\nTabla del {base} (1..{hasta})")
            for i in range(1, hasta + 1):  # bucle for clásico
                print(f"{base} x {i:>2} = {base*i}")
        elif op == 2:
            n = leer_int("Ingresa un entero ≥ 0: ")
            if n < 0:
                print("Debe ser ≥ 0.")
                continue
            # factorial con while
            fac = 1
            k = 1
            while k <= n:
                fac *= k
                k += 1
            print(f"{n}! = {fac}")
        else:
            print("Opción inválida.")


# ----------------------------- 5) Agenda con diccionario -----------------------------

def agenda_contactos():
    """
    Usa un diccionario para almacenar contactos:
    - Clave: nombre (str)
    - Valor: tupla (teléfono:str, email:str)
    Demuestra: diccionarios, tuplas, listas (para recorrer claves).
    """
    agenda: dict[str, tuple[str, str]] = {}

    def agregar():
        nombre = input("Nombre del contacto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        # Tupla para agrupar datos simples y mantenerlos inmutables
        agenda[nombre] = (telefono, email)
        print("Contacto guardado.")

    def listar():
        if not agenda:
            print("Agenda vacía.")
            return
        print("\nContactos:")
        # Convertimos a lista para poder ordenar por nombre
        for nombre in sorted(list(agenda.keys())):
            telefono, email = agenda[nombre]
            print(f"- {nombre}: {telefono} | {email}")

    def buscar():
        q = input("Buscar por nombre: ").strip()
        datos = agenda.get(q)
        if datos:
            telefono, email = datos
            print(f"Resultado: {q} -> {telefono} | {email}")
        else:
            print("No encontrado.")

    def eliminar():
        q = input("Eliminar por nombre: ").strip()
        if q in agenda:
            del agenda[q]
            print("Eliminado.")
        else:
            print("No encontrado.")

    while True:
        print("\n=== Agenda de Contactos ===")
        print("1) Agregar")
        print("2) Listar")
        print("3) Buscar")
        print("4) Eliminar")
        print("0) Volver")
        op = leer_int("Elige opción: ")
        if op == 0:
            return
        if op == 1:
            agregar()
        elif op == 2:
            listar()
        elif op == 3:
            buscar()
        elif op == 4:
            eliminar()
        else:
            print("Opción inválida.")


# ----------------------------- 6) Áreas geométricas con funciones -----------------------------

# Constante "global" de ejemplo (en mayúsculas por convención)
PI = 3.141592653589793

def area_circulo(r: float) -> float:
    """Área de un círculo: π * r^2."""
    return PI * (r ** 2)

def area_rectangulo(base: float, altura: float) -> float:
    """Área de un rectángulo: base * altura."""
    return base * altura

def area_triangulo(base: float, altura: float) -> float:
    """Área de un triángulo: (base * altura) / 2."""
    return (base * altura) / 2.0

def calculadora_areas():
    """
    Menú que llama funciones puras para calcular áreas.
    Demuestra modularización y reutilización.
    """
    while True:
        print("\n=== Calculadora de Áreas ===")
        print("1) Círculo")
        print("2) Rectángulo")
        print("3) Triángulo")
        print("0) Volver")
        op = leer_int("Elige opción: ")
        if op == 0:
            return

        if op == 1:
            r = leer_float("Radio: ")
            print(f"Área = {area_circulo(r):.4f}")
        elif op == 2:
            b = leer_float("Base: ")
            h = leer_float("Altura: ")
            print(f"Área = {area_rectangulo(b, h):.4f}")
        elif op == 3:
            b = leer_float("Base: ")
            h = leer_float("Altura: ")
            print(f"Área = {area_triangulo(b, h):.4f}")
        else:
            print("Opción inválida.")


# ----------------------------- Menú principal -----------------------------

def main():
    while True:
        print("\n==============================")
        print("  Portafolio Módulo 3 (Python)")
        print("==============================")
        print("1) Conversor de unidades")
        print("2) Formulario (tipos de datos)")
        print("3) Signo de un número")
        print("4) Iteraciones (tablas/factorial)")
        print("5) Agenda (diccionario)")
        print("6) Áreas geométricas (funciones)")
        print("0) Salir")

        op = leer_int("Elige una opción: ")
        if op == 0:
            print("¡Gracias! Fin del programa.")
            break
        elif op == 1:
            conversor_unidades()
        elif op == 2:
            formulario_usuario()
        elif op == 3:
            signo_de_numero()
        elif op == 4:
            tablas_o_factorial()
        elif op == 5:
            agenda_contactos()
        elif op == 6:
            calculadora_areas()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
