from typing import Callable

def left_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals):
        value += function(down_border + i * step)
    return step * value

def right_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals):
        value += function(down_border + (i + 1) * step)
    return step * value

def middle_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals):
        value += function(down_border + (i + 1 / 2) * step)
    return step * value

def trapezoid(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals + 1):
        if (i == 0):
            value += function(down_border)
        elif (i == count_of_intervals):
            value += function(up_border)
        else:
            value += 2 * function(down_border + i * step)
    return step / 2 * value

def simpson(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals + 1):
        if (i == 0):
            value += function(down_border)
        elif (i == count_of_intervals):
            value += function(up_border)
        else:
            value += 2 * function(down_border + i * step)
            value += 4 * function(down_border + (i + 1 / 2) * step)
    return step / 6 * value
