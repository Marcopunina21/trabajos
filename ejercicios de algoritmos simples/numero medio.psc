Algoritmo medio3numeros
	Definir n1,n2,n3 Como Entero;
	
	
	repetir 
		Escribir "Ingresa 3 numeros"; leer a,b,c;
		si (a > b y b > c ) o (a < b y c > b)  Entonces
			Escribir "El numero medio es: ",b;
		SiNo
			si (b > a y a > c) o (b < a y c > a)Entonces
				Escribir "El numero medio es: ",a;
			SiNo
				si (b > c y  c > a) o (b < c y a > c) Entonces
					Escribir "El numero medio es: ",c;
				FinSi
			FinSi		
		FinSi	
		
		
	Hasta Que a = b y b = c;
	
	

	
FinAlgoritmo