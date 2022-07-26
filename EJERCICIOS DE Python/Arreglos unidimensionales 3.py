# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 19:17:04 2022

@author: ldpc8
"""

def sumar(a, i=0, suma=0):
    if len(a) == i:
        return suma
    elif a[i] % 2 ==0:
        suma+=a[i]
    return sumar(a, i+1, suma)

print("Ingrese 10 numeros:")
a=[]
for x in range(10):
    x+=1
    z = int(input(f"Dato para vec[{x}]: "))
    a.append(z)
#Endfor   
print(sumar(a))