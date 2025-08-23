def convertir_temperatura(valor, unidad_origen, unidad_destino):
    # Si la unidad origen y destino son iguales, no se necesita conversión
    if unidad_origen == unidad_destino:
        return valor
    elif unidad_origen == 'C' and unidad_destino == 'F':
        return valor * 9/5 + 32
    elif unidad_origen == 'F' and unidad_destino == 'C':
        return (valor - 32) * 5/9
    elif unidad_origen == 'C' and unidad_destino == 'K':
        return valor + 273.15
    elif unidad_origen == 'K' and unidad_destino == 'C':
        return valor - 273.15
    else:
        return 'Conversión no soportada'

valor = float(input("Ingresa valor de temperatura: "))
unidad_origen = input("Unidad de origen (C/F/K): ").upper()
unidad_destino = input("Unidad destino (C/F/K): ").upper()

resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
print(f'Resultado: {valor} {unidad_origen} = {resultado} {unidad_destino}')
