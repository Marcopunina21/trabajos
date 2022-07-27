# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 23:32:37 2022

@author: ldpc8
"""

"""
Una compañía de seguros de autos quiere saber cuánto deben pagar en total por las
pólizas para un grupo de X personas. Para calcular la póliza de cada persona se ingresa
una cuota base(de 1 a 500 dólares) y sobre este valor se le carga 7% si la persona bebe
alcohol, 4% si utiliza lentes, y si tiene más de 40 años, se le carga 13%, de lo contrario
sólo 9%
"""
def cuota(c):
    if a == "si":
        c1=c+(c*0.07)
    if b == "si":
        c1=c+(c*0.04)
    if d == "si":
        c1=c+(c*0.13)
    else:
        c1=c+(c*0.09)
    c1+=c1
    print("La paga total es de: ",c1)
        
x = int(input("Ingrese la cantidad de personas: "))
i=1
for i in range(1,x+1):
        c = int(input(f"Cuota base de la persona {i}: "))
        if c>=1 and c<=500:
            i+=1
            a = input("La persona bebe alcohol 'si' o 'no': ")
            b = input("La persona utiliza lentes 'si' o 'no': ")
            d = input("La persona tiene mas de 40 años 'si' o 'no': ")   

cuota(c)
    
    

    
    