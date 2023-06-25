# Ejercicio 11.2: Crear una funcion para multiplicar todos los numeros en una lista o  tupla.

def multiplicar(valores):
    """
    multiplica el conjunto o grupo de valores de una lista o tupla:

    Parameters:
    Valores: Lista o tupla con los valores a multiplicar.

    Returns:
    multiplica de los valores en la lista o tupla.
    """
    if isinstance(valores, (list, tuple)):
        if len(valores):
            acumulador = 1

            for v in valores:
                acumulador *= v

            return acumulador
        else:
            return None
    else:
        raise ValueError('Ha pasado un argumento que no es lista ni tupla')
    
edades = [18,19,20,21]

try:
    resultado = multiplicar(edades)
    print('El resultado de multiplicar las edades {} es igual a {}.'.format(edades, resultado))
except ValueError as e:
    print('Error:', e)

print()

precios = (1000.91, 9983.92, 98.21)

try:
    resultado = multiplicar(precios)
    print('El resultado de multiplicar las edades {} es igual a {}.'.format(precios, resultado))
except ValueError as e:
    print('Error:', e)

print()

numeros = 1000
try:
    resultado = multiplicar(numeros)
    print('El resultado de multiplicar las edades {} es igual a {}.'.format(numeros, resultado))
except ValueError as e:
    print('Error:', e)

print()
numeros = []
try:
    resultado = multiplicar(numeros)
    if(resultado):
        print('El resultado de multiplicar las edades {} es igual a {}.'.format(numeros, resultado))
    else:
        print('Acabas de mandar una lista o tupla vacia')
except ValueError as e:
    print('Error:', e)