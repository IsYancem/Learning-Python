# Excepciones en flujo de ejecución de un programa Python.

try:
    numero = int(input('Escriba un numero entero:'))

    print()
    print('Contenido de la variable numero:', numero)
    print('El tipo de dato de la variable numero es:',type(numero))
except ValueError as e:
    print('Error:',e)

print()
print('El programa ha terminado')

print()

# Captura segura de un numero entero:
print('Captura segura de un numero entero:')

while True:
    try:
        edad = int(input('Digite su edad:'))

        if edad > 0:
            if edad <= 70:
                break
            else:
                print('MENSAJE: La edad no debe ser superior a los 70 anios')
        else:
            print('MENSAJE: El valor para la edad debe ser un numero positivo')
    except:
        print('MENSAJE: No ha escrito un valor valido. Intente de nuevo.')

print('Su edad es:', edad)


