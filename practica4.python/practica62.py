# practica 6 ejercicio 2
import math
cd = float(input("Ingrese el dinero inicial: "))
ta = int(input("Ingrese el tiempo en años: "))
it = float(input("Ingrese el interes: "))
z = round(cd*math.pow((1+it/100), ta), 2)
h = cd+z
k = round(h, 2)
j = str(k)
print(F"\nEl total de poliza: {j}")
