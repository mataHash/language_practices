// See https://aka.ms/new-console-template for more information
bool paroimpar(int numero)
{
    if (numero % 2 == 0)
    {
        Console.WriteLine("Es par");
        return true;
    }
    else
    {

        Console.WriteLine("Es impar");
        return false;
    }
}

paroimpar(12);
