while True:
    while True:
        hora=int(input("Ingrese una hora [hh]: "))
        if hora<0 or hora>23:
            print("El valor de las horas es incorrecto")
        else:
            break
    while True: 
        minutos=int(input("Ingrese los minutos [mm]: "))
        if minutos<0 or minutos>59:
            print("El valor de los minutos es incorrecto")
        else:
            break
    while True:
        segundos=int(input("Ingrese los segundos [ss]: "))
        if segundos<0 or segundos>59:
            print("El valor de los segundos es incorrecto")
        else:
            break
    while True:
        segundos2=int(input("Ingrese un valor en segundos: "))
        if segundos2<0:
            print("El valor de segundos debe ser positivo")
        else:
            x="0"
            ensegundos=(hora*3600)+(minutos*60)+segundos
            suma=segundos2+ensegundos
            hh=int(suma/3600)
            mm=int((suma/60)-(hh*60))
            ss=int((suma-(mm*60)-(hh*3600)))
            
            if hh<10 and mm<10 and ss<10:
                print("Nueva hora: ",x+str(hh),":",x+str(mm),":",x+str(ss))
                
            elif hh<10 and mm<10:
                print("Nueva hora: ",x+str(hh),":",x+str(mm),":",ss)
                
            elif mm<10 and ss<10:
                print("Nueva hora: ",hh,":",x+str(mm),":",x+str(ss))
                
            elif hh<10 and ss<10:
                print("Nueva hora: ",x+str(hh),":",mm,":",x+str(ss))
                
            elif hh<10 :
                print("Nueva hora: ",x+str(hh),":",mm,":",ss)
                
            elif mm<10 :
                print("Nueva hora: ",hh,":",x+str(mm),":",ss)
                
            elif ss<10 :
                print("Nueva hora: ",hh,":",mm,":",x+str(ss))
            break
        
    r=input("Si desea salir dijite NO, si desea cointinuar dijite cualquier tecla:  ")
    if r=="NO":
        break