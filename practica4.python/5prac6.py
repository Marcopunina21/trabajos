# Practica 6 ejercicio 5
n_elementos = int(input("Ingrese el numero de elementos: "))
valor_x = float(input("Ingrese el valor de x: "))

exponente = 1
factor_negativo = 1
serie = 0
for i in range(1, n_elementos+1):
    formula = (factor_negativo * ((valor_x**exponente)/(i*(i+1)*(i+2))))
    serie += formula
    #print(f'{factor_negativo}*{valor_x}**{exponente}/{i}*{i+1}*{i+2} = {formula}')
    # print(serie)
    exponente += 2
    factor_negativo *= -1

print('La serie es: {}'.format(serie))
