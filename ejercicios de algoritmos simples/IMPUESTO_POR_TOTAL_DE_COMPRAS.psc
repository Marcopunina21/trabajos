Algoritmo IMPUESTO_POR_TOTAL_DE_COMPRAS
	Definir ARTIC1,ARTIC2,ARTIC3,ARTIC4,ARTIC5,TOTALDELACOMPRA,IVA,TOTAL_CANCELAR	Como Real
	Escribir "INGRESE EL VALOR DEL ARTICULO1"
	Leer ARTIC1
	Escribir "INGRESE EL VALOR DEL ARTICULO2"
	Leer ARTIC2
	Escribir "INGRESE EL VALOR DEL ARTICULO3"
	Leer ARTIC3
	Escribir "INGRESE EL VALOR DEL ARTICULO4"
	Leer ARTIC4
	Escribir "INGRESE EL VALOR DEL ARTICULO5"
	Leer ARTIC5
	TOTALDELACOMPRA=(ARTIC1+ARTIC2+ARTIC3+ARTIC4+ARTIC5)
	Escribir "IVA"
	Leer IVA
	IVA=(TOTALDELACOMPRA*12/100)
	Escribir "TOTAL DE LA COMPRA:",ARTIC1,"+",ARTIC2,"+",ARTIC3,"+",ARTIC4,"+",ARTIC5, " ES: " TOTALDELACOMPRA
	Escribir "IVA:",TOTALDELACOMPRA,"*",12,"/",100, " ES: ", IVA
	TOTAL_CANCELAR=TOTALDELACOMPRA+IVA
	Escribir "TOTAL_CANCELAR:",TOTALDELACOMPRA,"+",IVA,"ES:", TOTAL_CANCELAR
FinAlgoritmo
