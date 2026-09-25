public class Facturacion
{
    public void ProcesarFactura(List<double> precios, List<int> cantidades, string tipoCliente)
    {
        double total = 0;
        void validacion_de_valores_no_nulos(List<double> precios, List<int> cantidades)
        {
            if (precios == null || cantidades == null)
            {
                Console.WriteLine("Error en datos");
            }
        }

        void validacion_de_cantidades_equivalentes(List<double> precios, List<int> cantidades)
        {
            if (precios.Count != cantidades.Count)
            {
                Console.WriteLine("Listas inconsistentes");
            }
        }
        void validacion_de_valores_positivos(List<double> precios, List<int> cantidades)
        {
            for (int i = 0; i < precios.Count; i++)
            {
                if (precios[i] <= 0)
                {
                    Console.WriteLine("Precio inválido");
                }

                if (cantidades[i] <= 0)
                {
                    Console.WriteLine("Cantidad inválida");
                }
                else
                {
                    total += precios[i] * cantidades[i];
                }
            }
        }

        double aplicar_descuento(string tipoCliente = "Regular")
        {
            double descuento_aplicado = 0;
            if (tipoCliente == "VIP")
            {
                descuento_aplicado = total - (total * 0.15);
            }
            else if (tipoCliente == "Regular")
            {
                descuento_aplicado = total - (total * 0.05);
            }
            return descuento_aplicado;
        }

        double aplicar_impuesto()
        {
            double impuesto = total * 0.18;
            return total = total + impuesto;
        }
        double aplicar_subtototal() { return 0; }
        void efectuar_operaciones()
        {
            Console.WriteLine("Subtotal con descuento: " + (total - aplicar_descuento()));
            Console.WriteLine("Impuesto: " + aplicar_impuesto());
            Console.WriteLine("Total final: " + total);
        }
    }
}
