from utils import *
from methods import *

print('\nПриближенное вычисление интегралов при помощи квадратурных формул Наивысшей Алгебраической Степени Точности')

while True:
    print(f'\nВыберите весовую функцию:\n1 - "{weight_1_string}",\n2 - "{weight_2_string}",\n3 - "{my_weight_string}",\n0 - Выйти')
    while True:
        decision = int_check('=> ')
        if decision not in [0, 1, 2, 3]:
            print('Такого значения нет в списке. Повторите ввод.')
            continue
        break
    match(decision):
        case 0:
            break
        case 1:
            down_border = -1
            up_border = 1
            weight = weight_1
            weight_string = weight_1_string
        case 2:
            down_border = -1
            up_border = 1
            weight = weight_2
            weight_string = weight_2_string
        case 3:
            down_border = float_check('Введите нижнюю границу интегрирования => ')
            up_border = float_check('Введите верхнюю границу интегрирования => ')
            weight = my_weight
            weight_string = my_weight_string

    print(f'Начальные данные:\n\tГраницы интегрирования: [{down_border}, {up_border}]')
    print(f'\tИнтеграл - {weight_string} * {function_string}')

    accurate_integral = get_value_of_integral(weight, down_border, up_border)
    if not accurate_integral.is_real:
        print('Вычисленный интеграл является комплекснозначным. Введите другие границы.')
        continue
    print(f'Точное значение интеграла - {accurate_integral}')

    print('\n\n"Вычисление интеграла с помощью ИКФ с N узлами"\n\n')

    count_of_points = positive_int_check("Введите количество узлов => ")
    print("Вводите попарно различные узлы: ")
    list_of_points = []

    for i in range(count_of_points):
        point = float_check(f'"x{i+1}" = ')

        while point in list_of_points:
            print("Такой узел уже есть, повторите ввод!")
            point = float_check(f'"x{i+1}" = ')

        list_of_points.append(point)

    list_of_values = [function(x) for x in list_of_points]

    coefficients = get_list_of_coefficients(down_border, up_border, list_of_points, weight)

    print("\nКоэффициенты ИКФ: ")
    for i in range(count_of_points):
        print(f"\tДля точки - {list_of_points[i]} коэффициент - {coefficients[i]}")

    print(f"\nПроведем проверку точности ИКФ на многочлене {count_of_points - 1} степени: ")

    polynomial_string = " + ".join([f"{i+1}*x^{i}" for i in range(len(list_of_points)-1, 0, -1)]) + " + 1"
    print(polynomial_string)

    quadrature_polynomial_integral, accurate_polynomial_integral = check_quadrature_formula(
        len(list_of_points) - 1, coefficients, list_of_points, down_border, up_border, weight
    )

    print(f'\n"Точное" значение интеграла от многочлена - {accurate_polynomial_integral}\n'
        f'Приближенное значение интеграла от многочлена - {quadrature_polynomial_integral}\n'
        f'Погрешность интеграла от многочлена - {abs(quadrature_polynomial_integral - accurate_polynomial_integral)}')

    quadrature_value = get_value_of_quadrature_formula(coefficients, list_of_values)

    print(f'\n"Точное" значение интеграла - {accurate_integral}')
    print(f'Значение интеграла, полученное с помощью ИКФ - {quadrature_value}')
    print(f'Погрешность вычисления - {abs(accurate_integral - quadrature_value)}')

    print('\n\n"Вычисление интеграла с помощью КФ НАСТ"\n\n')
   
    coefficients, nodes = get_list_of_coefficients_highest_degree(down_border, up_border, count_of_points, weight)
    quadrature_polynomial_integral, accurate_polynomial_integral = check_quadrature_formula_highest_degree(count_of_points, coefficients, nodes, down_border, up_border, weight)
    print(f'\nПроведем проверку точности КФ НАСТ на многочлене:\n0.175 * x^{2 * count_of_points - 1} - 2.55 * x + 1.125')
    print(f'\n"Точное" значение интеграла от многочлена - {accurate_polynomial_integral}\n'
        f'Приближенное значение интеграла от многочлена - {quadrature_polynomial_integral}\n'
        f'Погрешность интеграла от многочлена - {abs(quadrature_polynomial_integral - accurate_polynomial_integral)}')

    quadrature_value_highest_degree = get_value_of_quadrature_formula_highest_degree(nodes, coefficients)
    print(f'\n"Точное" значение интеграла - {accurate_integral}')
    print(f'Значение интеграла по КФ НАСТ - {quadrature_value_highest_degree}')
    print(f'Погрешность вычисления - {abs(accurate_integral - quadrature_value_highest_degree)}')
