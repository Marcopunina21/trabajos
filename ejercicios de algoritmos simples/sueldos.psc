//Realice un programa que determine e imprima el 
//promedio del sueldo de varios trabajadores considerando que se les descuenta 

Algoritmo sueldo
	Definir s,d,prom Como Real;
	k = 0;
	i = 0;
	Repetir
		i = i +1;
		Escribir "Cuanto recibe de salario el trabajador numero ",i; ; leer s;
		si s <= 450 y s >= 1 Entonces
			d = (5*s/100);
		SiNo
			si s > 450 y s < 600 Entonces
				d = (7*s/100);
			SiNo
				si s >= 600 Entonces
					d = (9*s/100);
				FinSi
			FinSi
		FinSi
		p = s - d;
		k = k + p;
		Escribir "Desea registrar el salario de otro trabajador (si = 1)(no = 0)"; Leer p;
	Hasta Que s <= 0 o s > 800 o p = 0
	prom = k/i;
	Escribir "El promedio de salario es: ",prom;
FinAlgoritmo
