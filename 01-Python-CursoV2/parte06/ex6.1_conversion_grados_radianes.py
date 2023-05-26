# Ejercicio 1. Convertir grados a radianes.
import math

grados = float(input('Inserte el numero de grados:'))

resultado = (math.pi * grados) / 180

print('El resultado es:{} radianes'.format(resultado))