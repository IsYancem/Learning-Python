# Ejercicio 11.1: Crear una funcion para obtener el mayor de tres numeros.

print('===== Programa para determinar el mayor de tres numeros =====')

numero1 = int(input('Digite el primer valor: '))
numero2 = int(input('Digite el segundo valor: '))
numero3 = int(input('Digite el tercer valor: '))

def numeroMayor (numero1, numero2, numero3): 
    mayor = 0

    if numero1 > mayor:
        mayor = numero1

    if numero2 > mayor:
        mayor = numero2

    if numero3 > mayor:
        mayor = numero3

    return mayor

resultado = numeroMayor(numero1, numero2, numero3)

print('El numero es:', resultado)
