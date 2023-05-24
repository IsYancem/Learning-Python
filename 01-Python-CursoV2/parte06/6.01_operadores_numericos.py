import math

# Operadores numericos

# Operador suma +

numero_1 = 2
numero_2 = 9

suma = numero_1 + numero_2

print(f'La suma de {numero_1} y {numero_2} es igual a {suma}')

print()

suma = 2 + 9
print(f'La suma de {numero_1} y {numero_2} es igual a {suma}')

print()

suma = numero_1 + 9
print(f'La suma de {numero_1} y {numero_2} es igual a {suma}')

print()

# Suma de n cantidad de elementos:
# Se pueden tener n cantidad de elementos a sumar
print('Se pueden tener n cantidad de elementos a sumar:')
suma = 1 + 2 + 3 + 4 + 5
print(f'La suma es igual a {suma}')

print()

# Suma de numeros reales (punto flotante):
print('Suma de numeros reales (punto flotante):')
numero_3 = 3.5896
suma =  numero_3 + 2.023 + 3.66 + 4.15 + 51.6
print(f'La suma es igual a {suma}')

numero_3 = 3.5896
suma =  numero_3 + numero_2 + numero_1
print(f'La suma es igual a {suma}')

suma =  7.81 + 2.023 + 3.66 + 4.15 + 51.6
print(f'La suma es igual a {suma}')

print()

# OPERADOR RESTA:
print('OPERADOR RESTA:')

numero_1 = 5
numero_2 = 2

resta = numero_1 - numero_2 # 5 - 2
print(f'La resta de {numero_1} y {numero_2} es igual a: {resta}')

print()

resta = numero_1 - 3
print(f'La resta de {numero_1} y {3} es igual a: {resta}')

print()

print('Expresion de resta de multiplos valores:')
resta = 5 - 6 - 1 - 4 - 12
print(f'La resta es igual a: {resta}')

print()

# Resta de valores numericos reales (punto flotante):
print('Resta de valores numericos reales (punto flotante):')

resta = 5.21 - 2.325 - 1.02
print(f'La resta es igual a: {resta}')

numero_1 = 598.25
numero_2 = 352.236
resta = numero_1 - numero_2 - 15
print(f'La resta es igual a: {resta}')

print()

# Invertir el signo de una literal numerica (entera o real) con el operador de resta (-):
print('Invertir el signo de una literal numerica (entera o real) con el operador de resta (-):')

numero = 100

print('El valor de variable numero es igual a:', numero)
print('El valor de variable numero es igual a:', -numero)
print('El valor de variable numero es igual a:', numero)

print()

numero = -100

print('El valor de variable numero es igual a:', numero)
print('El valor de variable numero es igual a:', -numero)
print('El valor de variable numero es igual a:', numero)

print()

pi = math.pi
print('El valor de la variable pi es igual a', pi)
print('El valor de la variable pi es igual a', -pi)

# OPERADOR PRODUCTO (MULTIPLICACION): *
print('OPERADOR PRODUCTO (MULTIPLICACION): *')

numero_1 = 7
numero_2 = 5

producto = numero_1 * numero_2
print(f'El producto de {numero_1} * {numero_2} es igual a: {producto}')

print()

print('Producto de dos literales:')

producto = 7 * 5
print(f'El producto de {7} * {5} es igual a: {producto}')

print()

print('Producto de una variable por un literal:')

numero_1 = 8
producto = numero_1 * 5
print(f'El producto de {numero_1} * {5} es igual a: {producto}')

print()

print('Producto de varios valores:')

producto = numero_1 * 5 * 9 * numero_2
print(f'El producto es igual a: {producto}')

print()

print('Producto de valores de punto flotante o reales:')

numero_1 = 8.25
numero_1 = 7.236
producto = numero_1 * 5.23 * 9.14 * numero_2
print(f'El producto es igual a: {producto}')

# Operador de división (decimales): /
print('Operador de división (decimales): /')

numero_1 = 1
numero_2 = 2

division = numero_1 / numero_2
print('La división de {} entre {} es igual a {}.'.format(numero_1, numero_2, division))

print()

print('División entre dos literales numéricas enteras:')

division = 1 / 2
print('La división de {} entre {} es igual a {}.'.format(1, 2, division))

print()

print('División entre una variable y una literal entera:')

division = numero_1 / 2
print('La división de {} entre {} es igual a {}.'.format(numero_1, 2, division))

print()

print('Expresión de división con múltiples operandos:')

division = 8 / 4 / 3 / 2

print('La expresión `8 / 4 / 3 / 2` es igual a', division)

print()

# División entre variables y literales numéricas reales (punto flotante):

print('División entre variables y literales numéricas reales (punto flotante):')

numero_1 = 0.5
numero_2 = 1.73

division = numero_1 / numero_2
print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))

print()

print('División de una variable y literal de punto flotante:')

division = numero_1 / 1.73
print('La división de {} y {} es igual a {}.'.format(numero_1, 1.73, division))

print()

print('División de literales de punto flotante (reales):')

division = 0.5 / 1.73
print('La división de {} y {} es igual a {}.'.format(0.5, 1.73, division))

print()

print('Múltiples diviones en una expresión:')

division = 0.5 / 1.73 / 4.5 / 7.0
print('La operación `0.5 / 1.73 / 4.5 / 7.0` es igual a:', division)

print()

# División entre cero:
print('División entre cero:')

numero_1 = 5
numero_2 = 0


print('Solución #1:')

if numero_2 != 0:
    division = numero_1 / numero_2
    print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))
else:
    print('MENSAJE: La división entre cero no está permitida.')

print()

print('Solución #2:')

try:
    division = numero_1 / numero_2
    print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))
except ZeroDivisionError as e:
    print('Error:', e)

print()

# Operador resto (residuo, módulo): %

# 5 // 2 = 2
# 5 % 2 = 1

numero_1 = 5
numero_2 = 2

division = numero_1 // numero_2
resto = numero_1 % numero_2

print(f'La división entera de {numero_1} y {numero_2} es igual a {division}.')
print(f'El resto de la división entera de {numero_1} y {numero_2} es igual a {resto}.')

print()

print('¿Es número par o impar?')

if numero_1 % 2 == 0:
    print('El valor {} es par.'.format(numero_1))
else:
    print('El valor {} es impar.'.format(numero_1))

print()

# Operador de división entera: //

numero_1 = 5
numero_2 = 2

division = numero_1 / numero_2

print(f'División entre {numero_1} y {numero_2} es igual a {division}.')

print()

division_entero = numero_1 // numero_2
print(f'División entera entre {numero_1} y {numero_2} es igual a {division_entero}.')

print()

# Operador de potencia: **
print('Operador de potencia: **')

base = 2
exponente = 3

potencia = base ** exponente

print(f'La potencia de {base}^{exponente} es igual a {potencia}.')

print()

potencia = pow(base, exponente)
print(f'La potencia de {base}^{exponente} es igual a {potencia}.')
