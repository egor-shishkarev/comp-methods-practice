def float_check(input_string: str):
    while (True):
        try:
            x = float(input(input_string))
            break
        except:
            print("Вы ввели неправильное значение, повторите ввод!")
    return x

def int_check(input_string: str):     
    while (True):
        try:
            x = int(input(input_string))
            break
        except:
            print("Вы ввели неправильное значение, повторите ввод!")
    return x
