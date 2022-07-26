# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:11:39 2022

@author: ldpc8
"""

""" 
Dado una matriz cuadrada de n filas y columnas, ingresar 
los datos solo con valores impares e imprimir la matriz 
de atrás hacia adelante.
"""

n = int(input("Ingrese el tama;o de la matriz cuadrada: "))
print("\nInserte solo numeros impares")
matriz_a=[[0 for col in range(n)] 
      for fil in range(n)]
for i in range(n):
    for j in range(n):
        matriz_a[i][j] = int(input(f"c{i}{j}: "))
        while matriz_a[i][j] % 2 == 0:
            matriz_a[i][j] = int(input(f"c{i}{j}: "))
        #Endwhile
    #Endfor
#Endfor

matrix_2 = []
for i in range(len(matriz_a)):
    matrix_2.append(matriz_a[i][::-1])
#Endfor
print("\nLa matriz original:")
for rows in matriz_a:
    print(rows)
#Endfor
print("\nLa matriz invertida:")
for rows in matrix_2:
    print(rows)
#Endfor


















