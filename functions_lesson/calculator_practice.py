import math_practice as m

def calculate(*args, operator):
    avaliable_actions = {'+': m.custom_add, '-': m.custom_sub, '*': m.custom_mul, '/': m.custom_div}
    if not avaliable_actions.get(operator):
        return "Invalid operation"
    return avaliable_actions.get(operator)(*args)


print(calculate(1, 0, operator='/'))