Algoritmo sin_titulo
	Definir cir,base,altura,radio Como Real
	Definir FG Como Real
	Repetir
		Escribir 'areas de figuras geometricas '
		Escribir '**********'
		Escribir 'ingrese una opcion '
		Escribir 'area del cuadrado digite 1'
		Escribir 'area del rectangulo digite 2'
		Escribir 'area del circulo digite 3'
		Escribir '**********'
		Leer FG
		Si FG=1 Entonces
			Escribir 'area de un cuadrado '
			Escribir 'ingrese el valor de la base '
			Leer base
			total <- base*base
			Escribir 'el area del cuadrado es '
			Escribir total
		SiNo
			Si FG=2 Entonces
				Escribir 'area de un rectangulo '
				Escribir 'ingrese el valor de la base '
				Leer base
				Escribir 'ingrese el valor de la altura '
				Leer altura
				total <- (base*altura)
				Escribir 'el area del rectangulo  es '
				Escribir total
			SiNo
				Si FG=3 Entonces
					Escribir 'ingrese el radio del circulo '
					Leer radio
					cir <- pi*(radio*radio)
					Escribir 'el radio del circulo   es '
					Escribir cir
				FinSi
			FinSi
		FinSi
		Escribir 'desea continuar '
		Leer b
	Hasta Que b='no'
FinAlgoritmo
