#POTENCIA

base = int(input('Base: '))
exponente = int(input('Exponente: '))

if base < 0 or exponente <0:
    print("ERROOR!!")       
else:
    resultado = base**exponente
    print('resultado:', resultado)


