"""
Написати програму, яка переміщає всі нулі у кінець списку.
Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
Порядок ненульових чисел має зберегтися!
"""

custom_list = [1, 0, 13, 0, 0, 0, 5]
list_without_zero = [el for el in custom_list if el != 0]
result = list_without_zero + [0] * custom_list.count(0)
# print(result)

# for el in custom_list:
#     if el != 0:
#         list_without_zero.append(el)

"""
Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд], 
потім перемножити цю суму на останній елемент вхідного масиву.

Не забудьте, що перший елемент масиву має індекс 0.

Для порожнього масиву результат завжди 0.
[1, 3, 5] => 30
[6] => 36
[] => 0
"""


test = []
list_of_even_index = [el for index, el in enumerate(test) if index % 2 == 0]
result_1 = sum(list_without_zero) * test[-1] if test else 0
# print(result_1)
# list_of_even_index = [for el in test]

# for index, el in enumerate(test):
#     if index % 2 == 0
#         result_1 += el



# if test:
#     result_1 = result_1 * test[-1]
# print(result_1)
#
# my_list = []
# list_len = len(my_list)
# half = list_len // 2
# if list_len % 2 == 0:
#     new_list = [my_list[:half], my_list[half:]]
# else:
#     new_list = [my_list[:half+1], my_list[half+1:]]
# print(new_list)


"""
1. Необхідно створіти список випадкових чисел із випадковою кількістю елементів від 3 до 10.

2. Створить інший список з 3 елементів зі списку з п.1 - першим, третім і другим з кінця.

"""

import random

random_number = random.randint(3, 10)
print(random_number)
random_list_numbers = [random.randint(1, 100) for _ in range(random_number)]
print(random_list_numbers)
result_of_elements = [random_list_numbers[0], random_list_numbers[2], random_list_numbers[-2]]
print(result_of_elements)

# for _ in range(random_number):
#     random_list_numbers.append(random.randint(1, 100))
# print(random_list_numbers)

import random

my_list = [random.randint(1,100) for i in range(random.randint(3, 10))]
list_selection = [my_list[0], my_list[2], my_list[-2]]
print(my_list)
print(list_selection)