# Ejercicio: 11.6 Usar una funcion para contar minusculas y mayusculas en una cadena.

def contador_minusculas_mayusculas(texto):
    """
    Cuenta la cantidad de letras mayusculas y minusculas en una cadena de texto

    Parameters:
    Texto: Cadena de caracteres

    Returns:
    Tupla con la cantidad de mayuculas y minusculas
    """
    if isinstance(texto, str):
        minusculas = 0
        mayusculas = 0

        for c in texto:
            if c.isalpha():
                if c.islower():
                    minusculas += 1
                if c.isupper():
                    mayusculas += 1
        
        return minusculas, mayusculas

    raise TypeError('El argumento debe ser una cadena')

frase = 'EmelEC CAmpeon'

try:
    resultado = contador_minusculas_mayusculas(frase)
    print('Cantidad minusculas:', resultado[0])
    print('Cantidad mayusculas:', resultado[1])
except TypeError as e:
    print('ERROR:', e)