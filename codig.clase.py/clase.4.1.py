partida1=int(input("ingrese el puntaje de la primera partida: "))
partida2=int(input("ingrese el puntaje de la segunda partida: "))
partida3=int(input("ingrese el puntaje de la segunda partida: "))
if partida1>=partida2 and partida3>=partida2:
    resultado=partida1+partida3

elif partida1>=partida3 and partida2>=partida3:
    resultado=partida1+partida2
    
else:
    resultado=partida2+partida3

print("El puintaje final es: " ,resultado)