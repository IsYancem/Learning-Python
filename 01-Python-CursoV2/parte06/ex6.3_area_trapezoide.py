# Ejercicio 3. Calcular área de un trapezoide.

print('Calcular el Area de un Trapezoide')
baseInferior = float(input('Inserte la base inferior:'))
baseSuperior = float(input('Inserte la base superior:'))
altura = float(input('Inserte la altura:'))

resultado = ((baseSuperior + baseInferior) / 2) * altura

print('El resultado es:{}'.format(resultado))
