//Desarrollar un algoritmo en pseudoc�digo que calcule la masa de aire de un neum�tico de autom�vil:
//m = pv / (t+ 460)0.37


Algoritmo masa1
	Definir p,v,t,m Como Real;
	escribir "Digite la presi�n en psi: "; Leer p;
	escribir "Digite el volumen en pies c�bicos: "; Leer v;
	escribir "Digite la temperatura en grados Fahrenheit: "; Leer t;
	
	m = p*v / ((t + 460) * 0.37);
	
	Escribir "La masa es: ",m," libras";
FinAlgoritmo
