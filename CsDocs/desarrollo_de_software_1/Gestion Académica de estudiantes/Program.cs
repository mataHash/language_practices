///<summary>
///</sumary>
class Program
{
    static List<string> estudiantes = new List<string>();
    static List<List<double>> notas = new List<List<double>>();

    static void Main()
    {
        int opcion = 0;

        while (opcion != 5)
        {
            MostrarMenu();
            int.TryParse(Console.ReadLine(), out opcion);

            switch (opcion)
            {
                case 1:
                    RegistrarEstudiante();
                    break;

                case 2:
                    AgregarNotas();
                    break;

                case 3:
                    MostrarPromedio();
                    break;

                case 4:
                    MostrarEstadisticas();
                    break;

                case 5:
                    Console.WriteLine("Saliendo del sistema...");
                    break;

                default:
                    Console.WriteLine("Opción inválida");
                    break;
            }
        }
    }

    static void MostrarMenu()
    {
        Console.WriteLine("\n===== SISTEMA DE GESTIÓN ACADÉMICA =====");
        Console.WriteLine("1. Registrar estudiante");
        Console.WriteLine("2. Agregar calificaciones");
        Console.WriteLine("3. Mostrar promedio de estudiante");
        Console.WriteLine("4. Mostrar estadísticas generales");
        Console.WriteLine("5. Salir");
        Console.Write("Seleccione una opción: ");
    }

    static void RegistrarEstudiante()
    {
        Console.Write("Nombre del estudiante: ");
        string nombre = Console.ReadLine() ?? "0";

        estudiantes.Add(nombre);
        notas.Add(new List<double>());

        Console.WriteLine("Estudiante registrado.");
    }




    static void AgregarNotas()
    {
        if (estudiantes.Count == 0)
        {
            Console.WriteLine("No hay estudiantes registrados.");
            return;
        }

        for (int i = 0; i < estudiantes.Count; i++)
        {
            Console.WriteLine($"{i} - {estudiantes[i]}");
        }

        Console.Write("Seleccione estudiante: ");
        int indiceNota;
        int.TryParse(Console.ReadLine(), out indiceNota);

        if (indiceNota < 0 || indiceNota >= estudiantes.Count)
        {
            Console.WriteLine("Estudiante inválido.");
            return;
        }

        Console.Write("¿Cuántas notas desea agregar? ");
        int cantidad;
        int.TryParse(Console.ReadLine(), out cantidad);

        for (int i = 0; i < cantidad; i++)
        {
            Console.Write($"Nota {i + 1}: ");
            double nota;
            double.TryParse(Console.ReadLine(), out nota);
            notas[indiceNota].Add(nota);
        }

        Console.WriteLine("Notas agregadas.");
    }

    static void MostrarPromedio()
    {
        if (estudiantes.Count == 0)
        {
            Console.WriteLine("No hay estudiantes registrados.");
            return;
        }

        for (int i = 0; i < estudiantes.Count; i++)
        {
            Console.WriteLine($"{i} - {estudiantes[i]}");
        }

        Console.Write("Seleccione estudiante: ");
        int indiceNota;
        int.TryParse(Console.ReadLine(), out indiceNota);

        if (indiceNota < 0 || indiceNota >= estudiantes.Count)
        {
            Console.WriteLine("Estudiante inválido.");
            return;
        }

        double promedio = CalcularPromedio(indiceNota);

        Console.WriteLine($"Promedio de {estudiantes[indiceNota]}: {promedio}");
    }

    static double CalcularPromedio(int indiceNota)
    {
        if (notas[indiceNota].Count == 0)
            return 0;

        double suma = 0;

        foreach (double nota in notas[indiceNota])
        {
            suma += nota;
        }

        return suma / notas[indiceNota].Count;
    }

    static void MostrarEstadisticas()
    {
        double sumaTotal = 0;
        int totalNotas = 0;

        double notaAlta = double.MinValue;
        double notaBaja = double.MaxValue;

        int aprobados = 0;
        int reprobados = 0;

        for (int i = 0; i < estudiantes.Count; i++)
        {
            double promedio = CalcularPromedio(i);

            if (promedio >= 70)
                aprobados++;
            else
                reprobados++;

            foreach (double nota in notas[i])
            {
                sumaTotal += nota;
                totalNotas++;

                if (nota > notaAlta)
                    notaAlta = nota;

                if (nota < notaBaja)
                    notaBaja = nota;
            }
        }

        double promedioGeneral = totalNotas > 0 ? sumaTotal / totalNotas : 0;

        Console.WriteLine("\n===== ESTADÍSTICAS =====");
        Console.WriteLine($"Promedio general: {promedioGeneral}");
        Console.WriteLine($"Nota más alta: {notaAlta}");
        Console.WriteLine($"Nota más baja: {notaBaja}");
        Console.WriteLine($"Aprobados: {aprobados}");
        Console.WriteLine($"Reprobados: {reprobados}");
    }
}
