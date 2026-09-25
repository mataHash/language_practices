// BIBLIOTECA DE FUNCIONES 
//
//
// Objetivo
//
//Crear una biblioteca de funciones matemáticas.
//Instrucciones
//
//    Crear métodos para: suma, resta, multiplicación, división
//    Crear métodos para: potencia, raíz cuadrada, factorial
//    Crear un menú que use estos métodos
//    Validar entradas en cada método
double suma(double Num1, double Num2) => Num1 + Num2;

double resta(double Num1, double Num2) => Num1 - Num2;

double producto(double Num1, double Num2) => Num1 * Num2;

double division(double Num1, double Num2)
{
    if (Num2 == 0) { return 0; }
    return Num1 - Num2;
}

double potencia(double Num1, double Num2) => Math.Pow(Num1, Num2);

double raiz(double Num1) => Math.Sqrt(Num1);

int nfactorial = 1;

int factorial(int Num1)
{
    while (Num1 >= 1)
    {
        nfactorial *= Num1;
        --Num1;
    }
    return nfactorial;
}

int caso = 0;
double num1 = 0.0;
double num2 = 0.0;
int menu()
{
    Console.WriteLine("Biblioteca de funciones!");
    Console.WriteLine("funciones disponibles:");
    Console.WriteLine("1. suma\n"
               + "2. resta\n"
               + "3. multiplicación\n"
               + "4. división\n"
               + "5. potencia\n"
               + "6. raíz cuadrada\n"
               + "7. factorial\n"
               + "8. Terminar");
    Console.Write("Seleccione un numero de funcion: ");
    caso = int.Parse(Console.ReadLine());
    switch (caso)
    {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            Console.Write("Inserte el primer numero: ");
            num1 = double.Parse(Console.ReadLine());
            Console.Write("Inserte el segundo numero: ");
            num2 = double.Parse(Console.ReadLine());
            break;
        case 6:
        case 7:
            Console.Write("Inserte el numero: ");
            num1 = double.Parse(Console.ReadLine());
            break;
        case 8:
            Console.Write("Terminado");
            break;
        default:
            Console.Write("Cometio un error");
            break;
    }
    return caso;
}
double resultado(int caso)
{
    switch (caso)
    {
        case 1:
            return suma(num1, num2);
        case 2:
            return resta(num1, num2);
        case 3:
            return producto(num1, num2);
        case 4:
            return division(num1, num2);
        case 5:
            return potencia(num1, num2);
        case 6:
            return raiz(num1);
        case 7:
            return factorial((int)num1);
        default:
            return -1;

    }
}
menu();
Console.Write("El resultado es: ");
Console.WriteLine(resultado(caso));
