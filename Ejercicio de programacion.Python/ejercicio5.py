# EJERCICIO 5 INDICE DE MASA CORPORAL
nombre = input('Nombre: ')
peso = float(input('Ingrese su peso (kg): '))
altura = float(input('Ingrese su altura: '))
imc = peso/(altura ** 2)
observacion = ''
if(imc < 18.5):
    observacion = 'bajo peso'
if(imc >= 18.5 and imc <= 24.9):
    observacion = 'normal'
if(imc >= 25.0 and imc <= 29.9):
    observacion = 'Sobrepeso'
if(imc > 30):
    observacion = 'obeso'
print(f"{nombre}tiene un Imc de: {round(imc,2)} k/m^2")
print(f'Observacion sobre peso:{observacion}')
