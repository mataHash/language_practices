// ver https://aka.ms/new-console-template para mas información
/* 

    Instalar Visual Studio Community [x]
    Crear un nuevo proyecto de consola[/]
    Escribir un programa que muestre tu 
    nombre, [/]
    carrera [/]
    y un mensaje de bienvenida[/]
    Ejecutar el programa y verificar que funciona correctamente[/]
 *
 * */
// Csharp usa tipado fuerte hay que declarar el tipo de dato
// nombre
string nombre = "Jorysniel Mata";
// carrera
string carrera = "Ingeniería de software";
// mensaje guarda un saludo en una cadena, y almacena nombre y carrera de forma concatenada y organizada
// este metodo utiliza formatted strings
string mensaje = $"Saludos! \n Mi Nombre es {nombre}, \n Estudio {carrera} y es un placer estar aqui";

// Console.writeline realiza un stdout(imprime o muestra en la consola) los datos especificados, en este caso el mensaje
Console.WriteLine(mensaje);
