# EJERCICIO 3: LLAMADAS TELEFONICAS
numero_telefonico = input('Ingrese el numero: ')
numero_de_la_hora = int(input('Ingrese la hora [0-23]: '))
numero_de_minutos = int(input('Ingrese los minutos [0-59]: '))

if(numero_de_la_hora >= 0 and numero_de_la_hora <= 8 and numero_de_minutos <= 20):
    print('CONTESTAR')

elif(numero_de_la_hora < 13 and numero_de_la_hora >= 8 and numero_de_minutos <= 20):
    if(numero_telefonico[-3:] == '909'):
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')

elif(numero_de_la_hora >= 13 and numero_de_la_hora <= 19 and numero_de_minutos <= 50):
    if(numero_telefonico[:3] == '877'):
        print("NO CONTESTAR")
    else:
        print('CONTESTAR')

elif(numero_de_la_hora >= 19  and numero_de_la_hora <=23 and numero_de_minutos >= 50):
    print('NO CONTESTAR')
