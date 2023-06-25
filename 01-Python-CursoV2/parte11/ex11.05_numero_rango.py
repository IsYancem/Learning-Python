# Ejercicio: 11.5 A traves de una funcion validar si un numero se halla en un rango.

def valorEnRango(valor, rango):
    """
    Comprueba si un valor dado se halla en un rango especifico

    Parameters:
    Valor: Valor del numero
    Rango: El rango especificado

    Returns:
    True si es verdad o false si es falsa
    """
    if isinstance(valor, (int, float)):
        if isinstance(rango, (list, tuple)):
            if len(rango) == 2:
                inicio = rango[0]
                final = rango[1]
                
                if inicio < final:
                    return valor in range(*rango)

                raise Exception('El ranfgo debe tener el incio menor al final')
            raise Exception('El ranfgo debe tener exactamente dos elementos')
        raise TypeError('Ha especificado un tipo de valor invalido para el argumento rango. Debe ser una lista o una tupla')
    raise TypeError('Ha especificado un tipo de valor invalido para el argumento valor. Debe ser entero o real')

numero = 5
rango = [0, 10]

try:
    resultado = valorEnRango(numero, rango)
    if resultado == True:
        print('El valor {} se halla en el rango {}.'.format(numero, rango))
    else:
        print('El valor {} no se halla en el rango {}.'.format(numero, rango))

except Exception as e:
    print('Error:',e)

print()

numero = 14
rango = [0, 10]

try:
    resultado = valorEnRango(numero, rango)
    if resultado == True:
        print('El valor {} se halla en el rango {}.'.format(numero, rango))
    else:
        print('El valor {} no se halla en el rango {}.'.format(numero, rango))

except Exception as e:
    print('Error:',e)