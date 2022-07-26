# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:57:52 2021

@author: lab
"""

"""
Don Juan vendió a 3 personas varias hectáreas de tierra a cada una. Cada hectárea cuesta 30000. Don 
Juan quiere saber el número de hectáreas que vendió en total, lo que le pagará cada uno de ellos 
(considerando un descuento del 7% por cada hectárea) y lo que le pagarán en conjunto considerando 
también el descuento.
"""

p1 = int(input("Cuantas hectareas le vendio a la persona 1: "))
p2 = int(input("Cuantas hectareas le vendio a la persona 2: "))
p3 = int(input("Cuantas hectareas le vendio a la persona 3: "))


h = 30000
d = (h*7)/100
k = h - d
x = p1 * k
y = p2 * k
z = p3 * k

print(f"En total vendio {p1+p2+p3} hectareas")
print(f"La persona 1 pagara {x} hectareas")
print(f"La persona 2 pagara {y} hectareas")
print(f"La persona 3 pagara {z} hectareas")
print(f"En conjunto le pagaran {x+y+z} dolares")













