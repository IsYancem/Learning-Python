# Parametros/argumentos nombrados variables - keywords:
print('Parametros/argumentos nombrados variables - keywords:')

def mostrar_identidad(**identificacion):
    resultado = ''

    if identificacion.get('cedula'):
        resultado += 'Cedula: ' + identificacion.get('cedula') + '\n'
    if identificacion.get('nombre'):
        resultado += 'Nombre: ' + identificacion.get('nombre') + '\n'
    if identificacion.get('apellido'):
        resultado += 'Apellido: ' + identificacion.get('apellido') + '\n'

    return resultado

persona = mostrar_identidad(nombre='Abraham', apellido='Yance')
print('Identificacion:', persona)

print()

persona = mostrar_identidad(nombre='Abraham', apellido='Yance', cedula='0955216270')
print('Identificacion:', persona)