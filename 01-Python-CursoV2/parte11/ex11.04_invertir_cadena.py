# Ejercicio: 11.4 Crear una funcion para invertir el contenido de una cadena de caracteres.

def invertir(texto):
    """
    Invierte una cadena de caracteres

    Parameters:
    Texto: Cadena de caracteres

    Returns:
    Cadena de caracteres invertido
    """
    if isinstance(texto, str):
        resultado = ''

        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]

        return resultado
    else:
        raise TypeError('No se ha especificado una cadena de texto')
    
frase = 'Emelec es el mas grande!'

try:
    resultado = invertir(frase)
    print('Texto orginal: {} - Texto invetido: {}'.format(frase, resultado))
except TypeError as e:
    print('Error:',e)

print()

frase = 1000

try:
    resultado = invertir(frase)
    print('Texto orginal: {} - Texto invetido: {}'.format(frase, resultado))
except TypeError as e:
    print('Error:',e)