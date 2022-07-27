# PRACTICA 4 EJERCICIO 3
horas = int(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa: "))
tasa = float(input("Ingrese la tasa: "))
pagab = horas*tarifa
impuestos = pagab*tasa
paganeta = impuestos-pagab

print("Su paga bruta es de: ", pagab, "Sus impuestos son igual a: ",
      impuestos, "Y su paga neta es igual a: ", paganeta)
