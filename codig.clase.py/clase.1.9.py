contador1=0
contador2=0
promedio=0
suma=0 
lista=[]
for i in range(1,6):
    valor=int(input("ingrese la altura: "))
    suma+=valor
    lista.append(valor)
promedio=suma/10
print("el promedio total es: ",promedio)
for j in range(5):
    if lista[j]>promedio:
        contador1+=1
    else:
        contador2+=1

print("hay",contador1,"mayor que el promedio")
print("hay",contador2,"menor que el promedio")