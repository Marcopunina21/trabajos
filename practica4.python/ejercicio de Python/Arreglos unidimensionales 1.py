# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:51:32 2022

@author: ldpc8
"""

"""Escribir un programa que permita llenar un vector con 
números 15 mayores a 50 (validar) mostrar la suma,
el promedio de los números del arreglo, así como el mayor y el menor"""

print("Ingrese 15 numeros:")
a=[]
for x in range(15):
    x+=1
    z = int(input(f"Dato para vec[{x}]: "))
    while z <= 50:
        z = int(input(f"Dato para vec[{x}]: "))
    a.append(z)
#Endfor   
dif_mayor = max(a)
dif_menor = min(a)
print("La suma es:",sum(a))
print("El promedio es:", int((sum(a)/15)))
print("El número mayor es:", dif_mayor)
print("El número mayor es:", dif_menor)

