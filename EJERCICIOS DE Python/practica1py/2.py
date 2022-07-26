# -- coding: utf-8 --
"""
Created on Thu Dec 16 19:05:32 2021

@author: ldpc8
"""
# Escribir un programa que permita ingresar un numero de 3 cifras y 
# que calcule el número de unidades, el número de decenas y el número de centenas. A continuación, se 
# visualizan los resultados de una posible salida del programa:
# Entrada: un número entero de 3 cifras
# Salida: número de unidades, el número de decenas y el número de centenas

print("-- UNIDADES DECENAS y CENTENAS --")
cifra = int(input("Ingrese un número entero de 3 cifras: "))
u = cifra // 100
q = cifra % 100
d = q // 10
h = q % 10
c = h
print(f"UNIDADES: {c}")
print(f"DECENAS: {d}")
print(f"CENTENAS: {u}")

