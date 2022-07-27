# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:27:51 2022

@author: ldpc8
"""

"""
Dados un arreglo de n valores enteros y un número leídos por teclado, eliminar el
número del arreglo todas las veces que coincida. Ejem. Arreglo es [2 4 6 8 3 7 3 7 9] y el
número es 3, el arreglo resultante es [2 4 6 8 7 7 9
"""
def remove():
    r = int(input("Que numero desea eliminar: "))
    print(q)
    posicion=0
    while posicion<len(q):
        if q[posicion]==r:
            q.pop(posicion)
        else:
            posicion=posicion+1
        #Endif
    #Endwhile
    print(q) 
    
n = int(input("Ingrese tamaño para el arreglo: "))
q=[]
for x in range(n):
    x+=1
    z = int(input(f"Ingrese el {x} numero: "))
    q.append(z)
#Endfor  
remove()









