def suma (*a):
    print("\n Tipo de datos del argumento: ",type(a))
    sum = 0
    for n in a:
        sum+=n
        #sum=suma+n
    print("suma: ",sum)
suma(3)
suma(1)
suma(3,5)
suma(3,4,5,6,7)