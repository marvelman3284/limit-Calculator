from math import sin, cos, tan, asin, acos, atan, pi, isclose
from rich import print
from time import sleep
from rich.prompt import Prompt


def sub(function: str, new_str: str) -> str:
    function = list(function)
    new_function = ""

    for _ in range(function.count("x")):
        function[function.index("x")] = f"({new_str})"

    for i in function:
        new_function += i

    return new_function


def calculate() -> str:
    function = input("Enter the function: ")
    c = int(input("Enter what number x is approaching: "))

    limit_table = [c - 0.01, c - 0.001, c - 0.0001, c + 0.0001, c + 0.001, c + 0.01]
    values = [eval(sub(function, i)) for i in limit_table]

    limit = (
        (
            round(values[0])
            if values[0] > 1
            else (
                round(values[0], 3)
                if isclose(values[2], values[4], rel_tol=0.1)
                else "D.N.E"
            )
        )
        if len(set([round(i) for i in values])) <= 1
        else "D.N.E"
    )

    return f"The limit of {function} as x approaches {c} is {limit}"


def main() -> None:
    help = Prompt.ask(
        "Would you like to view formatting help, calculate a limit or quit?",
        choices=["help", "calculate", "quit"],
    )

    if help == "help":
        print(
            "When you input the function include signs in between a constant and a variable ex: 3x+1 should be entered as 3*x+1"
        )
        print(
            "All trig function should be completely lowercase (ex: 'sin' or 'cos'). Any inverse trig function is 'a' + the function (ex: 'asin' or 'atan'). If you're trying to use PI it must be completely lowercase: 'pi'. Exponents should be writen with '**' instead of '^', and radicals should be used by raising to a fractional exponent.\n"
        )
        sleep(3)
        main()

    elif help == "calculate":
        print(calculate())

    elif help == "quit":
        quit()


if __name__ == "__main__":
    main()
