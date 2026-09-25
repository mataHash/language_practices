import turtle
import math


def polygon(t, length, n):
    t = turtle.Turtle()
    angle = (360/n)
    int(n)
    int(angle)
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    t = turtle.Turtle()
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)
