# Ejercicio 11.2: Crear una funcion para sumar todos los numeros en una lista o  tupla.

def sumar(valores):
    """
    Suma el conjunto o grupo de valores de una lista o tupla:

    Parameters:
    Valores: Lista o tupla con los valores a sumar.

    Returns:
    Suma de los valores en la lista o tupla.
    """
    if isinstance(valores, (list, tuple)):
        acumulador = 0

        for v in valores:
            acumulador += v

        return acumulador
    else:
        raise ValueError('Ha pasado un argumento que no es lista ni tupla')
    
edades = [18,19,20,21]

try:
    resultado = sumar(edades)
    print('El resultado de sumar las edades {} es igual a {}.'.format(edades, resultado))
except ValueError as e:
    print('Error:', e)

print()

precios = (1000.91, 9983.92, 98.21)

try:
    resultado = sumar(precios)
    print('El resultado de sumar las edades {} es igual a {}.'.format(precios, resultado))
except ValueError as e:
    print('Error:', e)

print()

numeros = 1000
try:
    resultado = sumar(numeros)
    print('El resultado de sumar las edades {} es igual a {}.'.format(numeros, resultado))
except ValueError as e:
    print('Error:', e)