from typing import Callable, List


def roots_separation(
        left_border: float,
        right_border: float,
        count_of_segments: int,
        function: Callable[[float], float]
        ) -> List[List[float]]:
    """
    Splits the given segment of function into smaller segments with one root \
        of odd degree.

    Args:
        left_border (float): Left border of the initial segment.
        right_border (float): Right border of the initial segment.
        count_of_segments (int): The number of segments into which we want to \
            split the original segment.
        function (Callable[[float], float]): The function for which we want to\
            find the roots.

    Returns:
        List[List[float]]: The found segments of the sign change.
    """

    h = (right_border - left_border) / count_of_segments
    x1 = left_border
    x2 = left_border + h
    root_segments: List[List[float]] = []

    while x2 <= right_border:
        y1 = function(x1)
        y2 = function(x2)
        if y1 * y2 <= 0:
            if len(root_segments) > 0:
                if root_segments[-1][1] != x1:
                    root_segments.append([x1, x2])
            else:
                root_segments.append([x1, x2])
        x1 = x2
        x2 = x1 + h
    return root_segments


def bisection_method(
        root_segment: List[float],
        function: Callable[[float], float],
        accuracy: float
        ) -> tuple[float, float, int]:
    """
    Searches for the root by bisection method - dividing the segment in half.

    Args:
        root_segment (List[float]): A segment with a single odd root of the \
            equation.
        function (Callable[[float], float]): The function for which we want to\
            find the roots.
        accuracy (float): Accuracy of the root approximation

    Returns:
        (tuple[float, float, int]): The approximate root, the inaccuracy of \
            the root, the number of iterations of the algorithm
    """
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


def newton_method(
        root_segment: List[float],
        function: Callable[[float], float],
        derivative: Callable[[float], float],
        accuracy: float
        ) -> tuple[float, float, int]:
    """
    Searches for the root by Newton's method - tangent approximation method

    Args:
        root_segment (List[float]): A segment with a single odd root of the \
            equation.
        function (Callable[[float], float]): The function for which we want to\
            find the roots.
        derivative (Callable[[float], float]): The derivative of the \
            introduced function
        accuracy (float): Accuracy of the root approximation

    Returns:
        (tuple[float, float, int]): The approximate root, the inaccuracy of \
            the root, and the number of iterations of the algorithm
    """

    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    x_prev = (a + b) / 2
    x_current = x_prev - (function(x_prev)) / (derivative(x_prev))

    while abs(x_current - x_prev) > accuracy:
        counter += 1
        x_prev = x_current
        x_current = x_prev - (function(x_prev)) / (derivative(x_prev))

    return (x_current, abs(x_current - x_prev), counter)


def modified_newton_method(
        root_segment: List[float],
        function: Callable[[float], float],
        derivative: Callable[[float], float],
        accuracy: float
        ) -> tuple[float, float, int]:
    """
    Searches for the root by modified Newton's method - tangent approximation \
        method,
    \nusing only f'(x0), where x0 - start point

    Args:
        root_segment (List[float]): A segment with a single odd root of the \
            equation.
        function (Callable[[float], float]): The function for which we want to\
            find the roots.
        derivative (Callable[[float], float]): The derivative of the \
            introduced function
        accuracy (float): Accuracy of the root approximation

    Returns:
        (tuple[float, float, int]): The approximate root, the inaccuracy of \
            the root, and the number of iterations of the algorithm
    """

    a = root_segment[0]
    b = root_segment[1]
    x0 = (a + b) / 2
    counter = 0

    x_prev = (a + b) / 2
    x_current = x_prev - (function(x_prev)) / (derivative(x0))

    while abs(x_current - x_prev) > accuracy:
        counter += 1
        x_prev = x_current
        x_current = x_prev - (function(x_prev)) / (derivative(x0))

    return (x_current, abs(x_current - x_prev), counter)


def secant_method(
        root_segment: List[float],
        function: Callable[[float], float],
        accuracy: float
        ) -> tuple[float, float, int]:
    """
    Searches for the root by secant approximation method

    Args:
        root_segment (List[float]): A segment with a single odd root of the \
            equation.
        function (Callable[[float], float]): The function for which we want to\
            find the roots.
        accuracy (float): Accuracy of the root approximation

    Returns:
        (tuple[float, float, int]): The approximate root, the inaccuracy of \
            the root, and the number of iterations of the algorithm
    """
    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    x_prev = a
    x_current = b
    if (function(x_current) - function(x_prev)) == 0:
        return (x_current, abs(x_current - x_prev), counter)
    x_next = (x_current - (function(x_current)) /
              (function(x_current) - function(x_prev)) *
              (x_current - x_prev))

    while abs(x_current - x_prev) > accuracy:
        counter += 1
        x_prev = x_current
        x_current = x_next
        if ((function(x_current) - function(x_prev)) == 0):
            return (x_current, abs(x_current - x_prev), counter)
        x_next = (
            x_current - (function(x_current)) /
            (function(x_current) - function(x_prev)) *
            (x_current - x_prev)
        )

    return (x_current, abs(x_current - x_prev), counter)
