def print_grid():
    print('+', end=' ')
    print(4 * '- ' + '+ ' + 4 * '- ' + '+')
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print('+', end=' ')
    print(4 * '- ' + '+ ' + 4 * '- ' + '+')
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")
    print("")
    print('+', end=' ')
    print(4 * '- ' + '+ ' + 4 * '- ' + '+')


def paralel_lines() -> None:
    print("| " + 4 * "  " + "| " + 4 * "  " + "| " + 4 * "  ")


def vertical_space() -> None:
    print("")


def start_end_lines() -> None:
    print('+', end=' ')
    print(4 * '- ' + '+ ' + 4 * '- ' + '+')


def paralel_body() -> None:
    for _ in range(4):
        paralel_lines()
        vertical_space()


def main_poligon() -> None:
    start_end_lines()
    vertical_space()
    paralel_body()
    start_end_lines()
    paralel_body()
    start_end_lines()


def main() -> None:
    print_grid()
    main_poligon()


if __name__ == "__main__":
    main()
