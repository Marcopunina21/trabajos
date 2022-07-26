
def sumar(n):
    calculo=0
    for i in range (1,n+1):
        calculo=calculo+2**i
    return calculo


N=int(input('N: '))
suma=sumar(N)
print(suma)
