from typing import Callable, Any


def do_twice(func: Callable[[Any], None], ar_2: str) -> None:
    func(ar_2)
    func(ar_2)


def print_spam(words: str) -> None:
    print(words)
    print(words)


def do_four(func: Callable[[Any], None], ar_2: str) -> None:
    do_twice(func, ar_2)
    do_twice(func, ar_2)


def main() -> None:
    do_twice(print, "spam")
    do_four(print, "spam")


if __name__ == '__main__':
    main()
