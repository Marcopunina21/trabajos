# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:42:45 2022

@author: USER
"""

bandera = True
#insertamos un while para que se repita mientras cumple ujna determina condicion
while bandera:
    #utilizamos el int(input) para mostrar en pantalla en valor de la variable
    n = int(input('Ingrese un numero: '))
    #utilizamos el if para tomar desiciones 
    #es decir una expresión que de como resultado True o False
    if n < 1:
        #al ingresar un numero menor que 1 nos emitira este mensaje
        print('Ingrese un numero mayor o igual 1')
    else:
        bandera = False
# Tabla de multiplicar con while
i = 1
while i < n:
    #mensaje para imprimir el N de la tabla
    print('La tabla del Numero ', i)
    i += 1
    #definimos todas las variables que van ser utilizadas
    tabla = 1
    suma = 0
    par = 0
    impar = 0
    promedio = 0
    #isertamos el while la cual nos indica hasta que numero de tabla va ejecutar
    while tabla < 16:
        multiplicacion = i*tabla
        #Formato de la tabla de multiplicar
        print(tabla, 'x', i, '=', multiplicacion)
        #calculo de las variables para la suma y promedio
        tabla += 1
        suma += multiplicacion
        promedio = suma//15
        #insertamos un if para determinar los numero paraes e impares
        if multiplicacion % 2 == 0:
            par = par+1
        else:
            impar = impar+1
            
print('-------------------------------------')
print('la suma es: ', suma)
print("El promedio de los numeros es:", promedio)
print("Hay", par, "numeros pares")
print("Hay", impar, "numeros impares")
print('')