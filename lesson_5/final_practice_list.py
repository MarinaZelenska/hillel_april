"""
******** метод - count() - розберемо через домашку
Написати програму, яка переміщає всі нулі у кінець списку.
Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
Порядок ненульових чисел має зберегтися!

**** метод sort()
first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2, 3, 14, 14]
first_list = ['test', 'abc', 'test', 'new', '123456']

first_list.sort(key=len, reverse=True)

*** copy()
import copy copy.deepcopy(first_list)

import copy

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2, 3, 14, 14, [1, 2]]
second_list = first_list.copy()
third_list = copy.deepcopy(first_list)
third_list[-1].append(3)
print(third_list)
print(first_list)


"""


