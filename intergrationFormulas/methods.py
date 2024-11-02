from typing import Callable

def left_rectangle(function: Callable[[float], float], down_border: float, up_border: float):
    return function(down_border) * (up_border - down_border)

def right_rectangle(function: Callable[[float], float], down_border: float, up_border: float):
    return function(up_border) * (up_border - down_border)

def middle_rectangle(function: Callable[[float], float], down_border: float, up_border: float):
    return function((up_border + down_border) / 2) * (up_border - down_border)

def trapezoid(function: Callable[[float], float], down_border: float, up_border: float):
    return(function(down_border) + function(up_border)) * (up_border - down_border) / 2

def simpson(function: Callable[[float], float], down_border: float, up_border: float):
    return (function(down_border) + 4 * function((down_border + up_border) / 2) + function(up_border)) * (up_border - down_border) / 6

def three_eighths(function: Callable[[float], float], down_border: float, up_border: float):
    step = (up_border - down_border) / 3

    return (up_border - down_border) * (
        1 / 8 * function(down_border)
        + 3 / 8 * function(down_border + step)
        + 3 / 8 * function(down_border + 2 * step)
        + 1 / 8 * function(up_border)
    )
