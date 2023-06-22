# Argumentos por defecto en un funcion:
print('Argumentos por defecto en un funcion:')

def saludar(nombre, saludo='Hola', pais='Ecuador'):
    """
    Saluda utilizando el saludo, nombre y pais

    Returns:
    Una frase saludando utilizando los parametros
    """
    
    frase = f'{saludo}, mi nombre es {nombre}, y soy de {pais}'

    return frase

resultado = saludar('Abraham', saludo='Buenos dias')

print('Resultado:', resultado)

print()

resultado = saludar('Jonathan', pais='Brasil')
print('Resultado:', resultado)

print()

resultado = saludar('Oliva', pais='Espania', saludo='Buenas noches')
print('Resultado:', resultado)

print()

def exponenciacion(base, exponente=2):
    """
    Calcula la exponenciacion de un numero base respecto a un exponente

    Parameters:
    base: Base de la exponeneciacion
    exponente: Potencia de la exponenciacion (valor por defecto 2).

    Returns:
    Exponenciacion de una base y un exponente
    """
    resultado = base ** exponente

    return resultado

potencia = exponenciacion(5)
print('El resultado de la exponenciacion es:', potencia)

print()

potencia = exponenciacion(10,3)
print('El resultado de la exponenciacion es:', potencia)
