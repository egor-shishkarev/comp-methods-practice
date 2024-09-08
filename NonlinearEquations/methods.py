from typing import Callable, List

def bisection_method(root_segment: List[float], function: Callable[[float], float], accuracy: float):
    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    while (b - a) > 2 * accuracy:
        counter += 1
        c = (a + b) / 2
        if (function(a) * function(c)) <= 0:
            b = c
        else:
            a = c
  
    x = (a + b) / 2
    delta = (b - a) / 2
    
    return (x, delta, counter)

def newton_method(root_segment: List[float], function: Callable[[float], float], derivative: Callable[[float], float], accuracy: float):
    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    x_prev = (a + b) / 2
    x_current = x_prev - (function(x_prev)) / (derivative(x_prev))

    while (abs(x_current - x_prev)) > accuracy:
        counter += 1
        x_prev = x_current
        x_current = x_prev - (function(x_prev)) / (derivative(x_prev))

    return (x_current, abs(x_current - x_prev), counter)


def modified_newton_method(root_segment: List[float], function: Callable[[float], float], derivative: Callable[[float], float], accuracy: float): 
    a = root_segment[0]
    b = root_segment[1]
    x0 = (a + b) / 2
    counter = 0

    x_prev = (a + b) / 2
    x_current = x_prev - (function(x_prev)) / (derivative(x0))

    while (abs(x_current - x_prev)) > accuracy:
        counter += 1
        x_prev = x_current
        x_current = x_prev - (function(x_prev)) / (derivative(x0))
        
    return (x_current, abs(x_current - x_prev), counter)

def secant_method(root_segment: List[float], function: Callable[[float], float], accuracy: float):
    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    x_prev = a
    x_current = b
    if ((function(x_current) - function(x_prev)) == 0):
        return (x_current, abs(x_current - x_prev), counter)
    x_next = x_current - (function(x_current)) / (function(x_current) - function(x_prev)) * (x_current - x_prev)

    while (abs(x_current - x_prev)) > accuracy:
        counter += 1
        x_prev = x_current
        x_current = x_next
        if ((function(x_current) - function(x_prev)) == 0):
            return (x_current, abs(x_current - x_prev), counter)
        x_next = x_current - (function(x_current)) / (function(x_current) - function(x_prev)) * (x_current - x_prev)
        
    return (x_current, abs(x_current - x_prev), counter)