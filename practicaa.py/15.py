# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:41:47 2022

@author: ldpc8
"""
"""
Dados 2 arreglos de flotantes igual o diferente tamaño, 
generar un tercer arreglo que resulta de unir los 
arreglos de forma alternada. Ejem. Arreglo1 [3 6 1 8 9 ], 
Arreglo2 [ 6 8 3 6], Arreglo resultante [3 6 1 8 9 6 8 3 6]
"""



n = int(input("Ingrese tamaño para el arreglo 1: "))
q=[]
for x in range(n):
    x+=1
    z = float(input(f"Ingrese el {x} numero: "))
    #Endwhile
    q.append(z)
#Endfor  
m = int(input("Ingrese tamaño para el arreglo 2: "))
h=[]
for i in range(m):
    i+=1
    f = float(input(f"Ingrese el {i} numero: "))
    #Endwhile
    h.append(f)
#Endfor  
c = q + h
print("Arreglo resultante: ",c)










