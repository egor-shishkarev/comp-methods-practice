from typing import List

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

def print_table(table: List[List[float]]):
    header_format = "{:<5} {:<25} {:<25}"
    row_format = header_format
    print()
    print(header_format.format('№', 'Точка', 'Значение в точке'))
    print('-' * 51)
    for i in range(len(table)):
        print(row_format.format(str(i + 1) + ')', table[i][0], table[i][1]))

def print_derivatives_table(table: List[List[float]]):
    header_format = "{:<4} {:<10} {:<15} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}"
    row_format = "{:<4} {:<10.6f} {:<15.6f} {:<20.10e} {:<20.10e} {:<20.10e} {:<20.10e} {:<20.10e} {:<20.10e}"
    print()
    print(header_format.format('№', 'xi', 'f(xi)', "f'(xi) 6-7-8", 'Погрешность', "f'(xi) новые", "Погрешность", "f''(xi) автор.", "Погрешность"))
    print('-' * 153)
    for i in range(len(table[0])):
        print(row_format.format(
            str(i + 1) + ')',
            table[0][i],
            table[1][i],
            table[2][i],
            table[3][i],
            table[4][i],
            table[5][i],
            table[6][i],
            table[7][i])
        )