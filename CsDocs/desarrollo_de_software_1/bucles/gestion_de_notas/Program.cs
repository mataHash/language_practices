double[] notas = new double[5];
bool aprobo = true;
int notas_aprobadas = 0;
for (int nota = 0; nota < 5; nota++)
{
    Console.WriteLine($"Inserte la nota #{nota + 1}");
    notas[nota] = Convert.ToDouble(Console.ReadLine());
    if (notas[nota] > 70)
    {
        notas_aprobadas += 1;
    }
}

Console.Write("Notas = ");
Console.WriteLine("[{0}]", string.Join(", ", notas));
double acumulado = 0;
double promedio = 0;
foreach (double valor in notas)
{
    acumulado += valor;
}
promedio = acumulado / notas.Length;
if (promedio > 70)
{
    aprobo = true;
}
else
{
    aprobo = false;
}
Console.WriteLine($"El promedio es: {promedio}");
Console.WriteLine($"promedio aprobado: {aprobo}");
Console.WriteLine($"notas aprobadas: {notas_aprobadas}");
double notaMayor = notas.Max();
Console.WriteLine($"nota Mayor: {notaMayor}");
double notaMenor = notas.Min();
Console.WriteLine($"nota Menor: {notaMenor}");


