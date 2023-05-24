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