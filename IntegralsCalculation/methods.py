from typing import List
import numpy as np
import sympy as sp
import scipy.linalg

def get_value_of_integral(down_border: float, up_border: float):
    x = sp.Symbol("x")
    p = sp.sin(x)
    f = 1 / sp.sqrt(x)

    result = sp.integrate(f * p, (x, down_border, up_border))
    return result.evalf(20)

def get_list_of_coefficients(
        down_border: float,
        up_border: float,
        list_of_points: List[float]
    ):
    matrix = np.array(_create_matrix(list_of_points), dtype=np.float64)
    weight_moments = np.array(_get_weight_moments(down_border, up_border, len(list_of_points)), dtype=np.float64)

    print("\nМоменты весовых функций: ")
    for i in range(len(list_of_points)):
        print(f"\tДля степени x = {i}: {weight_moments[i]}")

    coefficients = scipy.linalg.solve(matrix, weight_moments)
    return coefficients

def _create_matrix(list_of_points: List[float]):
    matrix = []
    for i in range(len(list_of_points)):
        row = []
        for j in range(len(list_of_points)):
            row.append(list_of_points[j] ** i)
        matrix.append(row)

    return matrix

def _get_weight_moments(
        down_border: float,
        up_border: float,
        count: int
    ):
    x = sp.Symbol("x")
    p = 1 / sp.sqrt(x)
    weight_moments = []

    for i in range(count):
        weight_moments.append(sp.integrate(p * (x ** i), (x, down_border, up_border)).evalf(20))

    return weight_moments

def check_quadrature_formula(
        degree: int, 
        coefficients: List[float],
        list_of_points: List[float],
        down_border: float,
        up_border: float
    ):
    # Пускай слагаемыми многочлена будут - 1, 2x, 3x^2, ...
    list_of_values = [0] * len(list_of_points)
    for i in range(len(list_of_points)):
        for j in range(degree + 1):
            list_of_values[i] += (j + 1) * list_of_points[i] ** j

    interpolation_integral = get_value_of_quadrature_formula(coefficients, list_of_values)

    x = sp.Symbol("x")
    polynomial = sum((i + 1) * x**i for i in range(degree + 1))
    weight_function = 1 / sp.sqrt(x)

    integrand = weight_function * polynomial
    accurate_integral = sp.integrate(integrand, (x, down_border, up_border)).evalf(15)

    return interpolation_integral, accurate_integral

def get_value_of_quadrature_formula(
        coefficients: List[float],
        list_of_values: List[float],
    ):
    interpolation_integral = 0
    for i in range(len(list_of_values)):
        interpolation_integral += coefficients[i] * list_of_values[i]

    return interpolation_integral
