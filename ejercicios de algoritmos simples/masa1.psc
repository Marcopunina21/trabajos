//Desarrollar un algoritmo en pseudocódigo que calcule la masa de aire de un neumático de automóvil:
//m = pv / (t+ 460)0.37


Algoritmo masa1
	Definir p,v,t,m Como Real;
	escribir "Digite la presión en psi: "; Leer p;
	escribir "Digite el volumen en pies cúbicos: "; Leer v;
	escribir "Digite la temperatura en grados Fahrenheit: "; Leer t;
	
	m = p*v / ((t + 460) * 0.37);
	
	Escribir "La masa es: ",m," libras";
FinAlgoritmo
