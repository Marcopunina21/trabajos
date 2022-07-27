# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 07:32:25 2022

@author: Alumno
"""
#Tabla de multiplicacion
# Dfinimos varuiables
suma=0                      
promedio=0
'''
Utilizamos el bucle for para que se repita el bloque de codigo
para todos los valores de una lista ,cadena o rango.
'''
for n in range(1,16):        
   print("")
   print("La tabla del N°:",n) #mostramos en pantalla las latblas de multiplicacion en el rango de 1 hasta 16. 
   print("")
   par=0
   impar=0
   '''
   volvemos utilizar el for dentro de un for 
   '''
   for i in range(1,16):
       #evaluamos las variables 
       res=i*n
       suma+=res
       promedio=suma//15
       print(i,"x",n,"=",res)
       '''
       "Cuando la expresión if se evalúa como par, 
       entonces ejecuta el código que le sigue. Pero si se evalúa
       como impar, entonces ejecuta el código que sigue después de la sentencia else.
       '''
       if res%2==0:
           par=par+1
       else:
           impar=impar+1
   '''
   Cuando print incluye una expresion, esta es evaluada antes de ser presentada
   en pantalla. puede imprimir varias expresiones separadas por comas 
   o traves de las cadenas.
   ''' 
   print("La suma de los numeros es",suma)
   print("El promedio de los numeros es:",promedio)
   print("Hay",par,"numeros pares")
   print("Hay",impar,"numeros impares")
   print("")
   