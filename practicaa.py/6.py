def sueldo():
    while True:
        op = input("Desea evaluar al empleado 'si' o 'no': ")
        if op == "si":
            for i in range(op == "si"):
                i+=1
                p=1
                for p in range(i):
                    p=p+1
                    c = float(input(f"Ingrese el sueldo del trabajador: {p}: "))
                if c >= 1 and c <= 450:
                    y = c - (c*0.05) 
                if c > 450 and c < 600:
                    y = c - (c*0.07) 
                if c < 600:
                    y = c - (c*0.09) 
                y+=y
                p=p+1
            continue
            p=p+1
            if c <= 0:
                   return c; 
                   return p
        if op == "no": 
            print(i)
            print("El promedio del sueldo de los empleados es: ",y/p)
            print("Adios");
        break;
            #Endfor
        #Endfor
    #Endwhile
#Enddef    
sueldo()  


 