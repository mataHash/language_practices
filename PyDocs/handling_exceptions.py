def asintopts(number: int) -> float:
    return 1 / number


def main():
    try:
        number = int(input("Enter a number: "))
        asintopts(number)
    except ZeroDivisionError:
        print("You cannot divide by zero idiot")
    except ValueError:
        print("Only Numbers dude")


if __name__ == "__main__":
    main()
