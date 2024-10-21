from utils import positive_int_check, float_check
from methods import *
from math import sqrt, sin
import numpy as np
import sympy as sp

#Вариант 3
# [𝑎, 𝑏] = [0, 1], 𝑓(𝑥) = sin(𝑥), 𝜌(𝑥) = 1 / sqrt(x)

function_string = "sin(x)"
weight_function_string = "1 / sqrt(x)"

def function(x):
    return sin(x)

def weight_function(x):
    return 1 / sqrt(x)

# 6. Сделать проверку на точность ИКФ на многочлене степени 𝑁 − 1, если 
# число узлов КФ равно 𝑁. Результаты проверки отразить на экране.

# 7. Вывести значение интеграла, полученное при помощи построенной ИКФ
# (не менее 12 знаков после запятой). 

# 8. Сравнить полученное при помощи ИКФ значение с "точным" значением из 
# матпакета

print("\nПриближённое вычисление интегралов при помощи интерполяционных квадратурных формул\n")
down_border = float_check("Введите нижнюю границу интегрирования => ")
up_border = float_check("Введите верхнюю границу интегрирования => ")

print(f'"Точное" значение интеграла по отрезку [{down_border}, {up_border}]',
      f'для функции ({function_string}) * ({weight_function_string}) = {get_value_of_integral(down_border, up_border)}')

count_of_points = positive_int_check("Введите количество узлов => ")
print("Вводите попарно различные узлы: ")
set_of_points = set()
for i in range(count_of_points):
    point = float_check(f'"x{i+1}" = ')
    try:
        previous_length = len(set_of_points)
    except (TypeError):
        previous_length = 0

    set_of_points.add(point)
    current_length = len(set_of_points)

    while previous_length == current_length:
        print("Такой узел уже есть, повторите ввод!")
        point = float_check(f'"x{i+1}" = ')
        set_of_points.add(point)
        current_length = len(set_of_points)

list_of_points = list(set_of_points)
coefficients = get_list_of_coefficients(weight_function, down_border, up_border, list_of_points)

for i in range(count_of_points):
    print(f"Для точки - {list_of_points[i]} коэффициент - {coefficients[i]}")
