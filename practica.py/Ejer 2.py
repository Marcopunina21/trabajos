# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:53:33 2022
@author: ldpc8
"""
# Números primos, pares, impares, promedio y mayor.
def esprimo(a):
    primos = []
    for i in a:
        p = 0
        if i == 1:
          primos.append(i)
        else:
          for j in range(1,i+1):
            if i % j == 0:
              p += 1
            #Endif
          #Endfor
          if p == 2:
            primos.append(i)
          #Endif
        #Endif 
    #Endfor 
    return primos
#Enddef
    
def paresimpares(lista):
    pares, impares = 0, 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        #Endif 
    #Endfor
    return pares, impares
#Enddef

def operation1(param):
    input("Presione una tecla para continuar . . .")
#Enddef

n = int(input("Ingrese tamaño para el vector: "))
a=[]
for x in range(n):
    z = int(input(f"Dato para vec[{x}]: "))
    x+=1
    a.append(z)
#Endfor   
resultado = paresimpares(a)
dif_mayor = max(a)
print()
print("Los números primos son: ",(esprimo(a)))
print("Los números pares son: %i" % resultado[0])
print("Los números impares son: %i" % resultado[1])
print("El número mayor es:", dif_mayor)
ret = operation1("")