# Gestion de excepciones para accesos de elementos a una lista:

lenguajes = ['Python', 'C++', 'JavaScript', 'Java', 'C', 'C#']

print('Cantidad de elemtnos de la lista lenguajes:', len(lenguajes))

print('Primer elemento de la lista lenguajes:', lenguajes[0])

print()

indice = 6

try:
    print('Ultimo elemento de la lista lenguajes:', lenguajes[indice])
except IndexError:
    print('El indice %i no existe en la lista lenguajes' % indice)

# print('El programa ha finalizado.')

print()

# Intento de acceso a indices negativos:
print('Intento de acceso a indices negativos:')

print('ultimo elemento de la lista lenguajes:', lenguajes[-1])

indice = -7

try:
    lenguaje = lenguajes[indice]

    print('Primer elemento de la lista lenguajes:', lenguaje)
except:
    print('El indice {} no existe en la lista lenguajes.'.format(indice))

print()

print('El programa ha terminado')
