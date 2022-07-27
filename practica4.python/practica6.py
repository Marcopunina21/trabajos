# practica 6 jercicio 1

x = int(input("Ingrese un numero del 1 al 100: "))

while x < 0 or x > 100:
    print("El numero no esta en el rango: ")
contador = 0

while contador < x:
    y = x*x
    x -= 1
    contador+1
    print(y)
