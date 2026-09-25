/*
 * "Realice un programa en C# que
 * muestre un menú con una 
 * cartelera de cine compuesta por 5 películas.
 * El usuario deberá ingresar un número del 1 al 5 y, 
 * utilizando una estructura switch, 
 * el programa deberá mostrar el nombre
 * de la película seleccionada junto con su horario de función.
 * Si el usuario ingresa un número fuera del rango, 
 * el programa deberá indicar que la opción es inválida."
        Ejemplo de cartelera:

        El Viaje del Héroe – 3:00 PM
        Amanecer Galáctico – 5:30 PM
        Leyendas del Caribe – 7:00 PM
        Código Oculto – 8:45 PM
        Misión Alfa – 10:15 PM
 */
Console.WriteLine(@" seleccione una pelicula:
1.El Viaje del Héroe – 3:00 Pm Precio 350
2. Amanecer Galáctico – 5:30 pm Precio 250
3.Leyendas del Caribe – 7:00 pm Precio 150
4. Código Oculto – 8:45 PM Precio 100
5.Misión Alfa – 10:15 PM Precio 50");

int pelicula = int.Parse(Console.ReadLine());
string mensaje = $"";
double precio = 0.0;
switch (pelicula)
{
    case 1:
        mensaje = "El Viaje del Héroe – 3:00 PM";

        precio = 350;
        break;
    case 2:
        mensaje = "Amanecer Galáctico – 5:30 PM";
        precio = 250;
        break;
    case 3:
        mensaje = "Leyendas del Caribe – 7:00 PM";
        precio = 150;
        break;
    case 4:
        mensaje = "Código Oculto – 8:45 PM";
        precio = 100;
        break;
    case 5:
        mensaje = "Misión Alfa – 10:15 PM";
        precio = 50;
        break;
    default:
        break;
}
Console.WriteLine($"has seleccionado {mensaje}");
Console.WriteLine($"Inserte el pago: ");
double Pago = double.Parse(Console.ReadLine());
if (Pago < precio)
{

    Console.WriteLine($"El pago realizado no es suficiente");
}
else if (Pago >= precio)
{

    Console.WriteLine($"has realizado el pago de {mensaje} con exito");
    Console.WriteLine($"Su devuelta es {Pago - precio}");
}

Console.WriteLine($"Su pelicula es {mensaje}");
