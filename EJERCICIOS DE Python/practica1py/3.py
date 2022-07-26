# -- coding: utf-8 --
"""
Created on Fri Dec 17 08:35:25 2021

@author: ldpc8
"""

# Ese desea visualizar los 2 nombres, los 2 apellidos y la nota final en programación 
# de un estudiante. Sabiendo que la nota se compone de la suma de 4 aportes, Deberes, Informes, 
# Pruebas y un Examen.
# Se sabe que los deberes aportan con 5 puntos a la nota general y que en total existen 3 deberes. Los 
# informes aportan con 10 puntos a la nota general y en total son 4 informes. Las pruebas aportan con 15 
# puntos a la nota general y son 2 pruebas. El examen aporta con 20 puntos a la nota general y existe un 
# solo examen.
# La nota general en ningún caso puede exceder los 50 puntos (5 puntos deberes + 10 puntos informes + 
# 15 puntos pruebas + 20 puntos examen generan un total de 50 puntos)
# A continuación, se visualizan los resultados de una posible salida del programa:
# Entrada: 3 notas para deberes, 4 notas para informes, 2 notas para pruebas, 1 nota para examen.
# Salida: Nota general

print("-- NOTA PROGRAMACION --")
print("Los deberes se califican sobre 5")
print("Los informes se califican sobre 10")
print("Las pruebas se califican sobre 15")
print("El examen se califica sobre 20")
nombr = input("Ingrese los nombres del estudiante: ")
apell = input("Ingrese los apellidos del estudiante: ")
d1 = float(input("Ingrese la nota del deber 1: "))
d2 = float(input("Ingrese la nota del deber 2: "))
d3 = float(input("Ingrese la nota del deber 3: "))
i1 = float(input("Ingrese la nota del informe 1: "))
i2 = float(input("Ingrese la nota del informe 2: "))
i3 = float(input("Ingrese la nota del informe 3: "))
i4 = float(input("Ingrese la nota del informe 4: "))
p1 = float(input("Ingrese la nota de la prueba 1: "))
p2 = float(input("Ingrese la nota de la prueba 2: "))
e = float(input("Ingrese la nota del examen: "))
dt = (d1 + d2 + d3)/3
it = (i1 + i2 + i3 + i4)/4
pt = (p1 + p2)/2
x = e + dt + it + pt
print(f"El señor {nombr} {apell} tiene una nota de {x} en programacion")









