// 
//Analizar un conjunto de datos usando arreglos.
//Instrucciones
//
//Crear un programa que:
//
//    Lea 10 números del usuario
//    Calcule suma, promedio, máximo y mínimo
//    Cuente números pares e impares
//    complejidad aproximada O(5n)
List<int> valor = new List<int>();
double suma = 0.0;
double promedio = 0.0;
double cantImpares = 0.0;
double cantPares = 0.0;
int numeroAUsar = 0;
int i = 1;
// bucle principal
while (i <= 10)
{
    Console.WriteLine($"entre el numero {i}");
    numeroAUsar = int.Parse(Console.ReadLine());
    valor.Add(numeroAUsar);
    i++;
}
// bucle para analisis
foreach (int numero in valor)
{
    suma += numero;
    promedio = suma / valor.Count();
    if (numero % 2 == 0)
    {
        cantPares += 1;

    }
    else
    {
        cantImpares += 1;
    }
}

double max = valor.Max();
double min = valor.Min();
Console.Write("numeros leidos: ");
Console.WriteLine("[{0}]", string.Join(", ", valor));
Console.WriteLine($"suma total: {suma}\n" +
        $"promedio: {promedio}\n" +
        $"Cantidad de numeros pares: {cantPares}\n" +
        $"Cantidad de numeros impares: {cantImpares}");

