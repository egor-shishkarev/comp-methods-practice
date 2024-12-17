from typing import Callable, List
from methods import *

def float_check(input_string: str) -> float:
    while (True):
        try:
            x = float(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x

def int_check(input_string: str) -> int:
    while (True):
        try:
            x = int(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x

def positive_int_check(input_string: str) -> int:
    while (True):
        x = int_check(input(input_string))
        if x <= 0:
            print('Вы ввели неположительное значение, повторите ввод!')
            continue
        break
    return x
