# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 20:00:45 2022

@author: ldpc8
"""
"""
Realizar la comprobación del dígito verificador del número de cédula. Usar un arreglo
de enteros para guardar los 9 primeros dígitos y realice los cálculos sobre cada valor
usando sus índices
"""
def funcion():
    a = 0
    for i in range(len(c) - 1):
        x = int(c[i])
        if i%2 == 0:
            x = x * 2
            if x > 9:
                x = x - 9
        a = a + x
    return a
c = input("Ingrese los 9 digitos de su cedula: ")
a = funcion()
if a%9 != 0:
    ver = 9 - (a%9) 
print("El ultimo y numero verificador es: ",ver)
print(str(c)+"-"+str(ver))