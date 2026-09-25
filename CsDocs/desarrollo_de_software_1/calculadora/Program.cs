// ver https://aka.ms/new-console-template para más información
string Titulo = "Mi calculadora";
Console.WriteLine(Titulo);
// leer el primer número
Console.WriteLine("Inserte el primer numero: ");
double num1 = Convert.ToDouble(Console.ReadLine());
//leer el segundo número
Console.WriteLine("Inserte el segundo numero: ");
double num2 = Convert.ToDouble(Console.ReadLine());
// operaciones
Console.WriteLine($"Suma:  {num1 + num2}");
Console.WriteLine($"Resta:   {num1 - num2}");
Console.WriteLine($"Multiplicación:  {num1 * num2}");
if (num2 == 0)
{

    Console.WriteLine("Dividir entre cero no es posible ");
}
else
{

    Console.WriteLine($"División:  {num1 / num2}");
}
