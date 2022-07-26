# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:15:55 2022

@author: USER
"""

import random

matrix = [ [ int ( ) for i in range ( 4 ) ] for j in range ( 4 ) ] 
# SE USA DOS FOR UNA PARA LAS FILAS Y OTRO PARA LAS COLUMNAS 
for filas in range ( 4 ) : 
    for columnas in range ( 4 ) : 
     # LLENAR LA MATRIZ CON LOS VALORES INGRESADOS 
        #valor = int ( input ( " Ingrese el valor : " ) ) 
        valor = random.randrange(1,100) 

        matrix [ filas ] [ columnas ] = valor 

for i in range ( 4 ) : 
    print ( " " , end = " " ) 
    for j in range ( 4 ) : 
        print ( matrix [ i ] [ j ] , " | " , end = " " ) 
    print ( " \ n " ) 
print ( matrix )


# Para sumar simplemente recorremos la matrix y aumentamos el valor
suma = 0
for valor in matrix:
    for numero in valor:
        suma = suma + numero

print(f"La suma es {suma}")

# Y el promedio se obtiene dividiendo la suma entre la cantidad de elementos
cantidad_elementos = len(matrix)
promedio = suma / cantidad_elementos
print(f"El promedio es {promedio}")