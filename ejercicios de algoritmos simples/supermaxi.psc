//Desarrollar un algoritmo que permita calcular el Total a pagar por las compras de varios artículos
//en el supermaxi. Considere que los artículos son variados y tienen diferentes precios. 
//Realizar el diagrama de flujo


Algoritmo supermaxi
	Definir total_pagar, total_art Como Real;
	
	repetir 
		Escribir "Ingrese el total de artículos: "; Leer total_art;
		Dimension art[total_art];
	
	Hasta Que total_art >= 0
	
		u = 1;
		Para u = 1 Hasta total_art
			Escribir sin saltar "Ingrese el precio del articulo numero ",u; Leer art[total_art];
			total_pagar = total_pagar + art[total_art];
		FinPara
		Escribir "EL TOTAL A PAGAR ES: ",total_pagar," DÓLARES" ;
		
	

FinAlgoritmo

