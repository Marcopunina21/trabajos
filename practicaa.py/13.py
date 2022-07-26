# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:00:31 2022

@author: ldpc8
"""

"""
Dadas las filas y columnas de una matriz(max. 10),
ingresar los datos e imprimir el promedio y 
también los valores mayores al mismo.
"""
def mayor():
    mayor  = matriz_a[0][0]
    for fila in matriz_a:
        for valor in fila:
            if valor > mayor:
                mayor = valor
    return mayor
(s , e) = 0,0
n = int(input("Ingrese el tamaño de la matriz: "))
while n > 10 or n < 1:
    n = int(input("Ingrese el tamaño de la matriz: "))
#Endwhile
matriz_a=[[0 for col in range(n)] 
      for fil in range(n)]
for i in range(n):
    for j in range(n):
        matriz_a[i][j] = int(input(f"c{i}{j}: "))
    #Endfor
#Endfor
for fila in matriz_a:
    for e in fila:
        s += e
        s += 1
p=s/(n*n)

print(f"El promedio es: {p-1}")

print(f"El mayor es {mayor()}")