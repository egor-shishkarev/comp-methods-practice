from utils import *
from math import sqrt, sin

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

print('\nПриближенное вычисление интегралов при помощи квадратурных формул Наивысшей Алгебраической Степени Точности\n')

down_border = float_check('Введите нижнюю границу интегрирования => ')
up_border = float_check('Введите верхнюю границу интегрирования => ')
down_border_original = -1
up_border_original = 1

print(f'Начальные данные:\n\tГраницы интегрирования: [{down_border}, {up_border}]')
print(f'\tФункция - {function_string}')

while True:
    print(f'\nВыберите весовую функцию:\n1 - "{weight_1_string}",\n2 - "{weight_2_string}",\n3 - "{my_weight_string}"')
    while True:
        decision = int_check('=> ')
        if decision not in [1, 2, 3]:
            print('Такого значения нет в списке. Повторите ввод.')
            continue
        break


# Три варианта веса - 1, 1 / sqrt(1 - x^2) - на [a, b]
# Вариант 3 [a, b] = [0, 1], f(x) = sin(x), p(x) = 1 / sqrt(x)



