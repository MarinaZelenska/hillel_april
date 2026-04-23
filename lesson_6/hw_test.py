"""
Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд], потім перемножити цю суму на останній елемент вхідного масиву.
Не забудьте, що перший елемент масиву має індекс 0.
Для порожнього масиву результат завжди 0.
"""
# lst = []
# sum_even_idx = 0
# for idx, el in enumerate(lst):
#     if idx % 2 == 0:
#         sum_even_idx += el
#
# sum_even_idx_mult_last = sum_even_idx * lst[-1] if len(lst) > 0 else 0
#
# print(f"Sum of elements with even indexes multiplied by last element in the list == {sum_even_idx_mult_last}")


"""
Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.

Змінна не може:

починатися з цифри
містити великі літери,
пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
бути жодним із зареєстрованих слів.
При цьому повне ім'я змінної може містити символ _, але не може містити два символи __ підряд.

Список зареєстрованих слів можна взяти із keyword.kwlist.

У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.


_ => True
__ => False
___ => False
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True
assert => False
assert_exception => True

"""

from string import punctuation, digits, ascii_uppercase
from keyword import kwlist

prohibited_symbols = punctuation.replace('_', ' ')

user_var = input('Please enter variable name: ')

is_keyword = user_var in kwlist
is_start_with_digits =  user_var[0] in digits
is_double_underline = '__' in user_var
is_contain_uppercase = False
is_contain_prohibited_symbols = False

for char in user_var:
    if char in prohibited_symbols:
        is_contain_prohibited_symbols = True
        continue
    if char in ascii_uppercase:
        is_contain_uppercase = True
        continue



is_var_valid = (not is_keyword and not is_contain_prohibited_symbols
                and not is_start_with_digits and not is_double_underline and not is_contain_uppercase)

print(f'Is your variable name \'{user_var}\' valid? {is_var_valid}')

