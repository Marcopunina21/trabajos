contador=0
contadornegativo=0
contadorigual=0
while True:
    while True:
        numero1=int(input("Ingrese el numero1: "))
        numero2=int(input("Ingrese el numero2: "))
        if numero1==numero2:
            print("Error los numeros no deven ser iguales")
            contadorigual+=1
        elif numero1<0 or numero2<0:
            print("Error los numeros no deven ser negativos")
            contadornegativo+=1
     
        else:
            break
    
    contador=contador+1
    print("Cuantas veces ",contador)
    print("cunatas veces igual ",contadorigual)
    print("cuantas veces negativo ",contadornegativo)
    salir=input(input("Si desea salir ingrese 0: "))
                
    if salir==0:
        break