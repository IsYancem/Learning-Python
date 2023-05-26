# Ejercicio 4. Calcular el área superficial y el volumen de un cilindro.

from math import pi

print('Calcular el area superficial y el volumen de un cilindro')

altura = float(input('Digite la altura(h):'))
radio = float(input('Digite el radio(r):'))

volumen = pi * (radio ** 2) * altura
areaSuperficial = (2 * pi * (radio ** 2)) + (2 * pi * radio * altura)

print('El volumen del cilindro es:{}'.format(volumen))
print('Elarea superficial del cilindro es:{}'.format(areaSuperficial))