from methods import *

def float_check(input_string: str) -> float:
    """
    Checks the entered value for float compliance

    Args:
        input_string (str): Input string

    Returns:
        float: Input value converted to float
    """

    while (True):
        try:
            x = float(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x

def int_check(input_string: str) -> int:
    """
    Checks the entered value for int compliance

    Args:
        input_string (str): Input string

    Returns:
        int: Input value converted to int
    """

    while (True):
        try:
            x = int(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x

def positive_int_check(input_string: str) -> int:
    while (True):
        x = int_check(input_string)
        if (x <= 1):
            print("Вы ввели значение меньшее либо равное 1, повторите ввод!")
            continue
        break
    return x
