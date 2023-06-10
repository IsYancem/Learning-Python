# Gestión de excepciones en operaciones aritméticas - división:
print('Gestión de excepciones en operaciones aritméticas - división:')

# Captura del primero número - dividendo:

while True:
    try:
        dividendo = float(input('Digite el dividendo:'))
        break
    except:
        print('MENSAJE: Debe escribir un valor valido. Intente de nuevo.')
    print()

while True:
    try:
        divisor = float(input('Digite el divisor:'))
        break
    except:
        print('MENSAJE: Debe escribir un valor valido. Intente de nuevo.')
    print()

try:
    division = dividendo / divisor
    print('El resultado de la division es:', division)
except ZeroDivisionError as e:
    print('ERROR:',e)
    print('MENSAJE: Intento de division entre cero.')
