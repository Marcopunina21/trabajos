# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:08:03 2022

@author: ldpc8
"""
"""
Considere que si el promedio de las N notas (comprendidas entre 1 y 10) 
de un alumno es mayor o igual a 9.1, se aplica un descuento del 15% 
en su matrícula, si es entre 7.0 y 9.0, el descuento es del 8%; 
de lo contrario, sólo se le aplica 6%. Se requiere saber cuánto
se pagarán en total por concepto de matrículas de un grupo de X alumnos.
"""
def validar():
    while True:
        k = int(input("Cual es la cantidad de alumnos: \n"))
        if k <= 0:
            continue
        else:
            return k
        #Endif
    #Endwhile
#Enddef

def validar2():
    while True:
        c = float(input("Ingrese el costo de las matriculas: "))
        if c <= 0:
            continue
        else:
            return c
        #Endif
    #Endwhile
#Enddef

h = 0
c = validar2()
k = validar()
for j in range(k):
    for i in range(10):
        x = float(input(f"Ingrese la nota {i+1} del alumno {j+1}: "))
        h+=x
        o = (h/10) 
    print(f"Promedio del alumno {j+1} es: ",o)
    if o >= 9.1:
            e = c - (c*0.15)
    elif o <= 9 or o >= 7:
            e = c - (c*0.08)
    else:
            e = c - (c*0.06)
    e+=e
        #Endif
    #Endfor
#Endfor
print(f"El total a parar por {k} alumnos es de: {e}")
 