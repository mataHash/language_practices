//
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Escriba su edad: ");
int edad = int.Parse(Console.ReadLine());
string categoría_de_vida = $"";
if (edad < 0)
{
    categoría_de_vida = " Su edad es invalida";
}
else if (edad <= 12)
{
    categoría_de_vida = "Niño";
}
else if (edad <= 17)
{
    categoría_de_vida = "Adolescente";
}
else if (edad < 39)
{
    categoría_de_vida = "Adulto Joven ";
}
else if (edad < 59)
{
    categoría_de_vida = "Adulto";
}
else
{
    categoría_de_vida = "Adulto Mayor";
}
Console.WriteLine($" Usted es {categoría_de_vida}");
