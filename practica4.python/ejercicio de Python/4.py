# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:01:38 2022

@author: ldpc8
"""
    
j=0
h=0
while True: 
    x = int(input("Digite la cantidad de alumnos: "))
    m1=0
    m2=0
    for i in range (1, x+1):
        a = int(input(f"Ingrese la edad del alumno {i}: "))
        b = float(input(f"Ingrese la estatura del alumno {i}: "))
        i+=1
        if a>18:
            m1=m1+1
        if b>1.75:
            m2=m2+1
        j+=a
        h+=b
    p = h/x
    print(f"La cantidad de mayores de 18 es: {m1}")
    print("El promedio de edad de los alumnos es: ",j//x)
    print(f"La cantidad con una estatura myor a 1.75 es: {m2}")
    print("EL promedio de estatura de los alumnos es: {:.2f}".format(p))
    break;
    
   



