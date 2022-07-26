# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:21:20 2022

@author: ldpc8
"""

# Numeros consecutivos

def resta_consecutivos(lista):
    b=[]
    for i in range(len(lista)-1):
        b.append(lista[i]-lista[i+1])
    #Endfor
    print("Diferencia entre números consecutivos: ")
    k=0
    for j in range(n-1):
        print (b[k])
        k+=1
    #Endfor
    dif_mayor = max(b)
    print("La diferencia mayor es:", dif_mayor)
#Enddef

n = int(input("Cuantos numeros desea ingresar?: "))
lista=[]
for x in range(n):
    z = int(input(f"Dato para vec[{x}]: "))
    x+=1
    lista.append(z)
#Endfor   

resta_consecutivos(lista)

