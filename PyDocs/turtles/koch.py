import turtle
from typing import Any


def koch(t: Any, length: int) -> None:
    t = turtle.Turtle()
    test(t, length)


def test(t: Any, length: float) -> None:
    if length > 3:
        test(t, length / 3)
        t.lt(60)
        test(t, length / 3)
        t.rt(120)
        test(t, length / 3)
        t.lt(60)
        test(t, length / 3)
    else:
        t.fd(length)


def main() -> None:
    koch("bob", 4203)
    turtle.mainloop()


if __name__ == "__main__":
    main()
