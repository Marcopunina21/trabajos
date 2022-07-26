# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:08:03 2022

@author: ldpc8
"""
"""
Realice un programa que lea un número e imprima el producto de la sumatoria de los
números pares e impares menores al ingresado. El proceso se repetirá hasta que
se introduzca un 0.
"""
def suma():
    i=m=k=0
    for i in range(1,e,2):        
        i+=e % 1
        k+=i
    print(f"\nLa suma de los impares es: {k}")
    print(" ")
    #Endfor
    for l in range(2,e,2):        
        l += e%1
        m+=l
    print(f"La suma de los pares es: {m}")            
    #Endfor
#Enddef
while True:
    e = int(input("Escriba un numero: "))
    if e >= 1:
        suma()
    else:
            break
    #Endif
#Endwhile












