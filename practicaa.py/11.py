# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:01:25 2022

@author: ldpc8
"""
"""
Dado una matriz cuadrada de n filas y columnas, ingresar los datos solo con valores
negativos e invertir la matriz (cambiar las filas por las columnas).
"""

def trans(u):
    t = []
    for i in range (len(u[0])):
        t.append([])
        for j in range(len(u)):
            t[i].append(u[j][i])
        #Endfor
    #Endfor
    return t
#Enddef

m = int(input("Ingrese el tama;o de la matriz cuadrada: "))
print("\nInserte solo numeros negativos")
matriz_a=[[0 for col in range(m)] 
      for fil in range(m)]
for i in range(m):
    for j in range(m):
        matriz_a[i][j] = int(input(f"c{i}{j}: "))
        while matriz_a[i][j] > -1:
            matriz_a[i][j] = int(input(f"c{i}{j}: "))
        #Endwhile
    #Endfor
#Endfor

print(); print(f"C = {matriz_a}")
print() ;print(f"C^t = {trans(matriz_a)}")

