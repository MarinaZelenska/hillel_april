


def custom_add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def custom_sub(*args):
    result = args[0]
    for arg in args:
        result -= arg
    return result

def custom_mul(*args):
    result = 0
    for arg in args:
        result *= arg
    return result

def custom_div(number_1, number_2):
    return number_1 / number_2 if number_2 != 0 else "Second number cannot be zero."