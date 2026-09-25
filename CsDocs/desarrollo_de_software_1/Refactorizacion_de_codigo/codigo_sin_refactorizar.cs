using System;
using System.Collections.Generic;

public class Facturacion
{
    public void ProcesarFactura(List<double> precios, List<int> cantidades, string tipoCliente)
    {
        double total = 0;

        if (precios == null || cantidades == null)
        {
            Console.WriteLine("Error en datos");
            return;
        }

        if (precios.Count != cantidades.Count)
        {
            Console.WriteLine("Listas inconsistentes");
            return;
        }

        for (int i = 0; i < precios.Count; i++)
        {
            if (precios[i] <= 0)
            {
                Console.WriteLine("Precio inválido");
                return;
            }

            if (cantidades[i] <= 0)
            {
                Console.WriteLine("Cantidad inválida");
                return;
            }

            total += precios[i] * cantidades[i];
        }

        if (tipoCliente == "VIP")
        {
            total = total - (total * 0.15);
        }
        else if (tipoCliente == "Regular")
        {
            total = total - (total * 0.05);
        }

        double impuesto = total * 0.18;
        total = total + impuesto;

        Console.WriteLine("Subtotal con descuento: " + (total - impuesto));
        Console.WriteLine("Impuesto: " + impuesto);
        Console.WriteLine("Total final: " + total);
    }
}
