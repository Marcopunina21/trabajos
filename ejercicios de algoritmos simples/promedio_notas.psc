// Desarrollar un algoritmo que permita calcular el promedio
// total de notas de un curso compuesto por un máximo de 25 estudiantes. 
// Considere que las notas están comprendidas entre 1 y 20 inclusive. 
// Realizar el diagrama de flujo
Algoritmo promedio_notas
	Definir alum Como Entero;
	Definir n Como Real;
	Repetir
		Escribir 'numero de alumnos';
		Leer alum;
	Hasta Que alum>=1 Y alum<=25
	Para i<-1 Hasta alum Hacer 
		Repetir
			Escribir 'Ingrese la nota del alumno ',i,' :';
			Leer n;
		Hasta Que n>=1 Y n<=20 
		k <- k+n;
	FinPara
	Escribir 'El promedio es: ',k/alum;
FinAlgoritmo
