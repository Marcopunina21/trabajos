# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:16:25 2022

@author: ldpc8
"""
# Multiplicacion de matrices
def pm(a, b):
    fa = len(a)
    fb = len(b)
    ca = len(a[0])
    cb = len(b[0])
    if ca != fb:
        return None
    p = []
    #Endif
    for i in range(fb):
        p.append([])
        for j in range(cb):
            p[i].append(None)
        #Endfor
    #Endfor
    for c in range(cb):
        for i in range(fa):
            suma = 0
            for j in range(ca):
                suma += a[i][j]*b[j][c]
            #Endfor
            p[i][c] = suma
        #Endfor
    #Endfor
#Enddef
    return p

m = int(input("Inserte las filas: "))
n = int(input("Inserte las columnas: "))
print("\n Matriz 1")
a=[[0 for col in range(n)] 
      for fil in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input(f"a{i}{j}: "))
    #Endfor
#Endfor
print("\n Matriz 2")
b =[[0 for col in range(n)] 
      for fil in range(m)]
for i in range(m):
    for j in range(n):
        b[i][j] = int(input(f"b{i}{j}: "))
    #Endfor
#Endfor
print(a, "*", b, "=")
p = pm(a, b)
for fila in p:
    for valor in fila:
        print(valor, end=" ")
    #Endfor
    print("")
#Endfor
