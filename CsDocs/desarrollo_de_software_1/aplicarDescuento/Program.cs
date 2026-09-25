double montoPago;
Console.Write("Inserte el numero a descontar: ");
montoPago = double.Parse(Console.ReadLine());


bool validarPago(double montoPago)
{
    if (montoPago >= 500)
    {

        return true;
    }
    else
    {
        return false;
    }

}
double mostrarDescuento()
{
    if (validarPago(montoPago))
    {
        return 50;
    }
    else
    {
        return 0;
    }
}
double aplicarDescuento()
{
    return montoPago - mostrarDescuento();
}
Console.WriteLine($"montoPagado: ${montoPago}\n" +
       $"Descuento aplicado:  {validarPago(montoPago)}\n" +
       $"monto a descontar:   ${mostrarDescuento()}\n" +
       $"total a pagar:   ${aplicarDescuento()}");
