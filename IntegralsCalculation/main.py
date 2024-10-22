from utils import positive_int_check, float_check
from methods import *
from math import sqrt, sin

# Вариант 3
# [𝑎, 𝑏] = [0, 1], 𝑓(𝑥) = sin(𝑥), 𝜌(𝑥) = 1 / sqrt(x)

function_string = "sin(x)"
weight_function_string = "1 / sqrt(x)"

def function(x):
    return sin(x)

def weight_function(x):
    return 1 / sqrt(x)

print("\nПриближённое вычисление интегралов при помощи интерполяционных квадратурных формул\n")

print(f"Номер варианта 3. Подынтегральная функция - {function_string} * {weight_function_string}\n")
down_border = float_check("Введите нижнюю границу интегрирования => ")
up_border = float_check("Введите верхнюю границу интегрирования => ")

print(f'\n"Точное" значение интеграла по отрезку [{down_border}, {up_border}]',
      f'для функции ({function_string}) * ({weight_function_string}) = {get_value_of_integral(down_border, up_border)}')

count_of_points = positive_int_check("Введите количество узлов => ")
print("Вводите попарно различные узлы: ")
list_of_points = []

for i in range(count_of_points):
    point = float_check(f'"x{i+1}" = ')

    # Проверяем, есть ли такой узел уже
    while point in list_of_points:
        print("Такой узел уже есть, повторите ввод!")
        point = float_check(f'"x{i+1}" = ')

    list_of_points.append(point)

list_of_values = [function(x) for x in list_of_points]

coefficients = get_list_of_coefficients(down_border, up_border, list_of_points)

print("\nКоэффициенты ИКФ: ")
for i in range(count_of_points):
    print(f"\tДля точки - {list_of_points[i]} коэффициент - {coefficients[i]}")

print(f"\nПроведем проверку точности ИКФ на многочлене {count_of_points - 1} степени: ")

# Создаем строковое представление многочлена
polynomial_string = " + ".join([f"{i+1}*x^{i}" for i in range(len(list_of_points)-1, 0, -1)]) + " + 1"
print(polynomial_string)

interpolation_integral, accurate_integral = check_quadrature_formula(
    len(list_of_points) - 1, coefficients, list_of_points, down_border, up_border
)

print(f'\n"Точное" значение интеграла от многочлена - {accurate_integral}\n'
      f'Приближенное значение - {interpolation_integral}\n'
      f'Погрешность - {abs(accurate_integral - interpolation_integral)}')

quadrature_value = get_value_of_quadrature_formula(coefficients, list_of_values)

print(f'\n"Точное" значение интеграла - {get_value_of_integral(down_border, up_border)}')
print(f'Значение интеграла, полученное с помощью ИКФ - {quadrature_value}')
print(f'Погрешность вычисления - {abs(get_value_of_integral(down_border, up_border) - quadrature_value)}')
