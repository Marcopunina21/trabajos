

# -*- coding: utf-8 -*-

"""
Es muy recurrente recibir llamadas no deseadas en tu celular. Para esto has decidido crear un
programa que te ayude a solucionar este problema dependiendo de:
• Hora de la llamada
• Número de teléfono
Tu misión es escribir un programa que decida por ti si contestarás a una llamada. Recibirás tres
enteros como entrada: teléfono y horario (horas y minutos). Si una llamada ocurre:
• entre 00:00 y 08:20 horas (incluyéndolas), sí contestarás, ya que podría ser una
emergencia.
• antes 13:00 horas (y después de las 08:20), no contestarás, excepto si el número termina
en 909.
• entre 13:00 y 19:50 (incluyéndolas), sí contestarás. Sin embargo, sabes que te llaman
regularmente de un número que comienza con 877 y prefieres no contestarle.
• después de las 19:50 y antes de la media noche, no contestarás ningún número
"""

a = int(input("Ingrese el número: "))
b = int(input("Ingrese la hora [0-23]: "))
c = int(input("Ingrese los minutos [0-59]: "))
d = b + (c/100)

if 0 <= d and d <= 8.20 :
        print("Contestar el telefono")
elif 8.20 < d and d < 13 :
    num6 = a % 1000
    if num6 == 909:
            print("Contestar el telefono")
    else:
            print("No contestar")
elif 13 < d and d <= 19.50 :
        num7 = a % 1000
        if num7 == 877:
            print("No contestar")
        else:
            print("Contestar el telefono")
elif 19.50 < d and d <= 23.59:
        print("No contestar")


