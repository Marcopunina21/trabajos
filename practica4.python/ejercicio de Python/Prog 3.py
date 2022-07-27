
# -*- coding: utf-8 -*-

"""
Desarrolle un programa que reciba como dato el nombre del pasajero, valor del pasaje, la edad y
nacionalidad. Si edad es menor o igual a 12 o mayor a 65 pero de nacionalidad ecuatoriana, tiene
un descuento del 40% en el valor de su pasaje. Desplegar el valor a pagar.:
"""
print("Digite su nombre y dos numeros enteros")
a = input("Ingrese el nombre del pasajero: ")
b = int(input("Ingrese el valor del pasaje: "))
c = int(input("Ingrese la edad: "))
d = input("Ingrese la nacionalidad: ")
f = b*0.40
g = b - f
if d == "ecuatoriana":
    if (12 >= c or c > 65):
        print(f"El descuento aplicado es de: {f}")
        print(f"El total a pagar por {a} es de: {round(g,2)}")
    else:
        print(f"El total a pagar por {a} es de: {round(g,2)}")
else:
    print(f"El total a pagar por {a} es de: {round(g,2)}")
