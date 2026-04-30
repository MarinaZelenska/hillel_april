"""
Розпаковка елементів по змінним та дістати елементи з ітерабельного об'єкту

"""

# a, b, c = 1, 2, 3  # [1, 2, 3], 'abc'
#
# print(a)
# print(b)
# print(c)

"""
Підхід з зірочкою
"""

# *a, b = 1, 2, 3
# a, *b, c = 'abcdefg' # наприклад треба тільки перший та останній елемент
# print(a)
# print(b)
# print(c)


"""
Дістати все з itarable data type
"""

# print(*[1, 2, 3, 4, 'test'])


"""
тепер поговоримо про функції
позиційні та ключові аргументи
"""
#
# def example(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# example(1, 2, 3)


"""
тепер про args kwargs
"""

def example(*args, **kwargs):
    print(args)
    # print(kwargs)
    # print(args, **kwargs)
    for arg in args:
        print(arg, **kwargs)

# example(1,2,3, end='-')

# print(1, 2, 3, sep=':', end='$')