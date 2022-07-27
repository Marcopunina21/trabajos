# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:42:22 2022

@author: ldpc8
"""
# Suma y promedio.

print("Ingrese 10 numeros:")
a=[]
for x in range(10):
    x+=1
    z = int(input(f"Dato para vec[{x}]: "))
    a.append(z)
#Endfor   

print("La suma es:",sum(a))
print("El promedio es:", int((sum(a)/10)))
