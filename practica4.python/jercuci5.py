# practica 4 ejercio 5
fosforos = int(input("Ingrese la cantidad de fosforos producidos: "))

caja = int(fosforos/40)
paquete = int(caja/12)
cajassob = int(fosforos % caja)
paquetesob = int(fosforos % paquete)
print("La cantidad de cajas es:", caja, "Y la cantidad de paquetes producidos es: ", paquete,
      "La cantidad de cajas sobrantes es: ", cajassob, "La cantidad de paquetes sobrantes es: ", paquetesob)
