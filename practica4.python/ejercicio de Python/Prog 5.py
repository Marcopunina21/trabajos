# JERCICIO 6 VENTA DE ROLLOS DE ALAMBRE
a = int(input("Cantidad de metros: "))
if a > 0:
    b = int(a/500)
    c = int(a % 500)
    d = int(c/300)
    e = int(a % 300)
    f = int(e/75)
    g = int(e % 75)
    print(f"{b} rollos de 500 metros, {d} rollos de 300 metros, {f} rollos de 75 metros y {g} metros")
else:
    print("Ingrese un numero positivo mayor a cero")
