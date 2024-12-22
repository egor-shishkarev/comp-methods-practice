from math import sqrt, sin
import sympy as sp
import numpy as np
from typing import List, Callable
import scipy.linalg
from scipy.integrate import quad

def weight_1(x: float):
    return 1

def weight_2(x: float):
    return 1 / sqrt(1 - x **2)

def my_weight(x: float):
    return 1 / sqrt(x)

def function(x: float):
    return sin(x)

weight_1_string = "1"
weight_2_string = "1 / sqrt(1-x^2)"
my_weight_string = "1 / sqrt(x)"
function_string = "sin(x)"

def get_value_of_quadrature_formula_highest_degree(nodes: List[float], coefficients: List[float]):
    quadrature_value = 0
    for i in range(len(nodes)):
        quadrature_value += function(nodes[i]) * coefficients[i]
    return quadrature_value

def get_list_of_coefficients_highest_degree(
        down_border: float,
        up_border: float,
        count: int,
        weight: Callable[[float], float], ):
    weight_moments = _get_weight_moments(down_border, up_border, 2 * count, weight)
    print('Моменты весовых функций КФ НАСТ:')
    for i in range(len(weight_moments)):
        print(f'\tДля степени x = {i}: {weight_moments[i]}')
    matrix = []
    for i in range(count):
        row = []
        for j in range(count):
            row.append(weight_moments[i + j])
        matrix.append(row)
    matrix = np.array(matrix, dtype=np.float64)
    column = [-weight_moments[i] for i in range(count, 2 * count)]
    column = np.array(column, dtype=np.float64)
    coefficients_of_equation = np.array(scipy.linalg.solve(matrix, column)) # коэффициенты уравнения
    print('Найденный ортогональный многочлен:')
    polynomial_string = ""
    polynomial_string += f'x^{count}'
    for i in range(len(coefficients_of_equation)):
        polynomial_string += f'+{coefficients_of_equation[i]}*x^{count - i - 1}'
    print(polynomial_string.replace('+-', '-').replace('*x^0', ''))
    nodes = np.array(np.roots(np.append(coefficients_of_equation, 1)[::-1]))
    print('Узлы КФ НАСТ:')
    for i in range(len(nodes)):
        print(nodes[i], end = ' ')
    coefficients = []
    for i, xi in enumerate(nodes):
        def lagrange_basis(x):
            basis = 1
            for j, xj in enumerate(nodes):
                if i != j:
                    basis *= (x - xj) / (xi - xj)
            return basis
        
        Ai, _ = quad(lambda x: lagrange_basis(x) * weight(x), down_border, up_border)
        coefficients.append(Ai)

    print('\nКоэффициенты КФ НАСТ:')
    for i in range(len(coefficients)):
        print(coefficients[i], end = ' ')

    return coefficients, nodes

def check_quadrature_formula_highest_degree(
        degree: int, 
        coefficients: List[float],
        nodes: List[float],
        down_border: float,
        up_border: float,
        weight: Callable[[float], float],
    ):
    # Многочлен вида 0.175*x^(2N-1) - 2.55*x + 1.125
    list_of_values = []
    for i in range(len(nodes)):
        print(f'Узел - {nodes[i]}')
        list_of_values.append(0.175 * nodes[i] ** (2 * degree - 1) - 2.55 * nodes[i] + 1.125)
        print(f'Полученное значение - {list_of_values[i]}')
    print(f'\nПолученные значения - {list_of_values}')

    quadrature_integral = 0
    for i in range(len(list_of_values)):
        quadrature_integral += list_of_values[i] * coefficients[i]
        
    x = sp.Symbol("x")
    polynomial = 0.175 * x ** (2 * degree - 1) - 2.55 * x + 1.125
    weights = {
        weight_1: 1,
        weight_2: 1 / sp.sqrt(1 - x ** 2),
        my_weight: 1 / sp.sqrt(x)
    }
    weight_function = weights.get(weight)

    integrand = weight_function * polynomial
    accurate_integral = sp.integrate(integrand, (x, down_border, up_border)).evalf(15)

    return quadrature_integral, accurate_integral


#!------------------------------------------- Методы из задачи 4.1 -------------------------------------------


def get_value_of_integral(weight: Callable[[float], float], down_border: float, up_border: float):
    x = sp.Symbol("x")
    f = sp.sin(x)
    functions = {
        weight_1: 1,
        weight_2: 1 / sp.sqrt(1 - x ** 2),
        my_weight: 1 / sp.sqrt(x)
    }
    p = functions.get(weight)

    result = sp.integrate(f * p, (x, down_border, up_border))
    return result.evalf(20)

def get_list_of_coefficients(
        down_border: float,
        up_border: float,
        list_of_points: List[float],
        weight: Callable[[float], float],
    ):
    matrix = np.array(_create_matrix(list_of_points), dtype=np.float64)
    weight_moments = np.array(_get_weight_moments(down_border, up_border, len(list_of_points), weight), dtype=np.float64)
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
        count: int,
        weight: Callable[[float], float],
    ):
    x = sp.Symbol("x")
    weights = {
        weight_1: 1,
        weight_2: 1 / sp.sqrt(1 - x ** 2),
        my_weight: 1 / sp.sqrt(x)
    }
    p = weights.get(weight)
    weight_moments = []

    for i in range(count):
        weight_moments.append(sp.integrate(p * (x ** i), (x, down_border, up_border)).evalf(20))

    return weight_moments

def check_quadrature_formula(
        degree: int, 
        coefficients: List[float],
        list_of_points: List[float],
        down_border: float,
        up_border: float,
        weight: Callable[[float], float],
    ):
    # Пускай слагаемыми многочлена будут - 1, 2x, 3x^2, ...
    list_of_values = [0] * len(list_of_points)
    for i in range(len(list_of_points)):
        for j in range(degree + 1):
            list_of_values[i] += (j + 1) * list_of_points[i] ** j

    interpolation_integral = get_value_of_quadrature_formula(coefficients, list_of_values)

    x = sp.Symbol("x")
    polynomial = sum((i + 1) * x**i for i in range(degree + 1))
    weights = {
        weight_1: 1,
        weight_2: 1 / sp.sqrt(1 - x ** 2),
        my_weight: 1 / sp.sqrt(x)
    }
    weight_function = weights.get(weight)

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