a=100
def isPrime(num):
    contador=0
    for i in range (1,num+1):
        if num%i==0:
            contador+=1
            print(i)
    if contador==2:
        return True
    else:
        return False
print(isPrime(a))  