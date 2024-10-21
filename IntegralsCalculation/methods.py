from typing import Callable, List
import numpy as np
import sympy as sp
import scipy.linalg

def get_value_of_integral(down_border: float, up_border: float):
    x = sp.Symbol("x")
    p = sp.sin(x)
    f = 1 / sp.sqrt(x)

    result = sp.integrate(f * p, (x, down_border, up_border))
    return result.evalf(30)

def get_list_of_coefficients(
        weight_function: Callable[[float], float],
        down_border: float,
        up_border: float,
        list_of_points: List[float]
    ):
    matrix = np.array(_create_matrix(list_of_points), dtype=np.float64)
    weight_moments = np.array(_get_weight_moments(weight_function, down_border, up_border, len(list_of_points)), dtype=np.float64)

    print("Моменты весовых функций: ")
    for i in range(len(list_of_points)):
        print(f"Для степени x = {i}: {weight_moments[i]}")

    coefficients = scipy.linalg.solve(matrix, weight_moments)
    return coefficients

def _create_matrix(list_of_points: List[float]):
    matrix = [[]]
    for i in range(len(list_of_points)):
        for j in range(len(list_of_points)):
            matrix[i].append(list_of_points[j] ** i)

        matrix.append([])
    matrix = matrix[:-1]

    return matrix

def _get_weight_moments(
        weight_function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count: int
    ):
    x = sp.Symbol("x")
    p = sp.sin(x)
    weight_moments = []

    for i in range(count):
        weight_moments.append(sp.integrate(p * (x ** i), (x, down_border, up_border)).evalf(20))

    print(weight_moments)

    return weight_moments
