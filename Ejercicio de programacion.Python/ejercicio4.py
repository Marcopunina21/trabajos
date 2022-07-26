# EJERCICIO 4 COSTO DEL PASAJE
pasajero = input('Ingrese el nombre del pasajero: ')
pasaje = int(input('Ingrese el valor del pasaje: '))
edad = int(input('Ingrese la edad: '))
nacionalidad = input('Ingrese la nacionalidad:')

descuento = 0.40
total = 0

if(edad <= 12 or edad > 65):
    total = pasaje*descuento

    if(nacionalidad == 'ecuatoriana'):
        total = pasaje*descuento

descuento = pasaje-total

print('El descuento total es de: ', total)
print(f'El total a pagar por juan {pasajero} es de: {descuento}')
