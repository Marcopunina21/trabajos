# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:44:08 2022

@author: ldpc8
"""

"""Escribir un programa que lea 5 números y los guarde en un vector. 
A continuación, los ordenará y mostrará
los valores ordenados. Mostrar el vector antes y después de ordenar"""

print("Ingrese 5 numeros:")
a=[]
for x in range(5):
    x+=1
    z = int(input(f"Dato para vec[{x}]: "))
    a.append(z)
#Endfor   
print(a)
b = sorted(a)
print(b)
