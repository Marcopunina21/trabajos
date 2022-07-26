# numeros primos
def isPrime(num, n=2):
    if n >= num:
        print(f"El numero {num} es primo")
        return True
    elif num % n != 0:
        return isPrime(num, n + 1)
    else:
        print(f"El numero {num} no es primo")
        return False


for i in range (1,21):
    isPrime(i)


