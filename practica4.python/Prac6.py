#practica 6 ejercicio 3
n = t = 0
while n <= 0:
    n = int(input('Tamaño del paquete: '))
while t <= 0:
    t = int(input("Tamaño basico del paquete del envio: "))
    print('     |',end='')
    for i in range(1, t+1):
        print(f"{n*i}", end="\t")
    print()
    for i in range(1, t*10):
        print("_", end="")
    print()
    for i in range(1, 11):
        print(i*10, "  |",end='')
        for j in range(1, t+1):
            print(round((j*n)/(i*10), 1),end='\t')   
        print()
