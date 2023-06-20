# Lista variable de argumentos de una funcion:
print('Lista variable de argumentos de una funcion:')

# def sumar(a, b):
#     return a + b

# def sumar(a, b, c):
#     return a + b + c

# def sumar(a, b, c, d):
#     return a + b + c + d

def sumar(*valores):
    suma = 0

    for v in valores:
        suma += v
    
    return suma

print()

resultado = sumar(1, 2)
print('El resultado de la suma es igual a:', resultado)

print()

resultado = sumar(1, 2, 3)
print('El resultado de la suma es igual a:', resultado)
