Algoritmo sin_titulo
	Definir num,impares,cuadrado Como Real
	Definir procedimiento Como Caracter
	Escribir 'Ingrese un numero a cacular: '
	Leer num
	impares <-1
	cuadrado <-0
	procedimiento <-''
	Para i <-1 Hasta num Con Paso 1 Hacer
		cuadrado<-cuadrado+impares
		procedimiento<-procedimiento+ConvertirATexto(impares)+'+'
		impares<-impares+2
	FinPara
	Escribir num,'^2=',procedimiento,'=',cuadrado
FinAlgoritmo
