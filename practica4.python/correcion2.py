seguir = True
while seguir:

    hora = int(input("Ingrese una hora: "))
    minutos = int(input("Ingrese el valor en minutos: "))
    segundos = int(input("Ingrese un valor en segundos: "))
    error = False
    # validacion de la hora
    if hora > 23 or hora < 0:
        print("el dato de la hora no es correcto")   
        error = True
    if minutos < 0 or minutos > 59:
        print(" El dato de los minutos no es coreecto")
        error = True
    if segundos < 0 or segundos > 59:
        print("El dato de losn segundos no es correcto")
        error = True
    if error == False:
        print("Puede continuar")
        sextra = int(input("Ingrese el valor de los segundos extras: "))
        if sextra < 0:
            print("El valor de los segundos extras es invalido")
        else:
            print("Puede coontinuar")
            ensegundos = (hora*3600)+(minutos*60)+segundos
            suma = sextra+ensegundos
            hh = int(suma/3600)
            mm = int((suma/60)-(hh*60))
            ss = int((suma - (mm*60)-(hh*3600)))
            if hh < 10:
                hh = f'0{hh}'
            if mm<10:
                ss=f'0{mm}'
            if ss<10:
                ss=f'0{ss}'
            print('Nueva hora: 'f'{hh}:{mm}:{ss}')
    print("====================================================")
    print('Presione S para continuar')
    print('Presione cualquier tecla  para salir')
    texto = input('Ingrese la opcion: ')
    if texto == 's':
        seguir = True
        print("====================================================")

    else:
        seguir = False
        print("Fin del programa")
