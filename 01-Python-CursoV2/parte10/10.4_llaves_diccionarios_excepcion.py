# Excepciones a la hora de trabajar con diccionarios.

versiones = {'python': '3.8.1', 'Java': '12', 'JavaScript': 'ES6', 'C#': '8'}

lenguaje = input('Escriba un lenguaje de programacion:')

try: 
    version = versiones[lenguaje]
    print('La version de {} es {}.' .format(lenguaje, version))
except KeyError as e:
    print('ERROR:', e)
    print('MENSAJE: El lenguaje no existe en el diccionario lenguajes')

print('El programa ha finalizado')

print()

# Uso del método `get()`:
print('Uso del método `get()`:')

version = versiones.get('java', '1.0.0')
print('La versión de {} es {}'.format('java', version)) 