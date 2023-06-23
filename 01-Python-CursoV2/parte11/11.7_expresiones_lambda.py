# Expresiones lambda - Funciones anonimas
print('Expresiones lambda - Funciones anonimas')

def sumar(a, b):
    return a + b

x = 2
y = 3

print('la suma de {} + {} es igual a {}'.format(x, y, sumar(x, y)))

print()

sumar_lambda = lambda a, b: a + b
print('la suma de {} + {} es igual a {}'.format(x, y, sumar_lambda(x, y)))

print()

def cuadrado(n):
    return n ** 2

cuadrado_lambda = lambda n: n ** 2

numero = 10

print('El cuadrado de {} es igual a {}'.format(numero, cuadrado(numero)))
print('El cuadrado de {} es igual a {}'.format(numero, cuadrado_lambda(numero)))

print()

# Filtrar el contenido de una lista:
print('Filtrar el contenido de una lista:')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Contenido de la variable numeros:', numeros)
print('Cantidad de elementos en la lista numeros:', len(numeros))

def extrear_impares(lista):
    impares = []

    for n in lista:
        if n % 2 != 0:
            impares.append(n)

    return impares

print()

resultado = extrear_impares(numeros)

print('Contenido de la variable numeros:', resultado)
print('Cantidad de elementos en la lista numeros:', len(resultado))

print()

resultado = [n for n in numeros if n % 2 != 0 ]
print('Contenido de la variable numeros:', resultado)
print('Cantidad de elementos en la lista numeros:', len(resultado))

print()

resultado = list(filter(lambda n: n% 2 != 0, numeros))
print('Contenido de la variable numeros:', resultado)
print('Cantidad de elementos en la lista numeros:', len(resultado))

print()

def filtro(n):
    return n % 2 != 0

resutlado = list(filter(filtro, numeros))
print('Contenido de la variable numeros:', resultado)
print('Cantidad de elementos en la lista numeros:', len(resultado))

print()

# Utilizar la funcion map() para crear un mapeo (mapping) del contenido de una lista (iterable)
def elevar_cuadrado(lista):
    cuadrados = []

    for n in lista:
        cuadrados.append(n ** 2)

    return cuadrados

resultado = elevar_cuadrado(numeros)
print('Contenido de la variable numeros:', numeros)
print('Contenido de la lista numeros al cuadrado:', resultado)

print()

resultado = [n ** 2 for n in numeros]
print('Contenido de la lista numeros al cuadrado:', resultado)

print()

resultado = list(map(lambda n: n ** 2, numeros))
print('Contenido de la lista numeros al cuadrado:', resultado)

