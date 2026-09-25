import turtle


def koch(size, n):                  # Dibujar curva de Koch
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


koch(30, 5)
