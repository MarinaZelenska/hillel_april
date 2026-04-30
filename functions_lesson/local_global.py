
"""
Working case
"""
# counter = 1
#
# def increment():
#     print(counter)
#
# increment()



"""
Invalid case
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value

Потому что переменная локальная
"""

#
# counter = 1
#
# def increment():
#     counter += 1
#     print(counter)
#
# increment()


"""
Щоб вирішити проблему global and nonlocal

Але тільки якщо треба змінювати значення змінної, але для того щоб вивести значення - то не потрібно( виняток enclosing scope)
"""


# counter = 1
#
# def increment():
#     global counter
#     counter += 1
#     print(counter)
#
# increment()
# increment()
# increment()


"""
Благодаря global ми можемо створити змінну в глобальному скоупі зсередини функції - погана практика

"""

# def increment():
#     global counter
#     counter = 100
#     print(counter)
#
# increment()
# increment()
# increment()
# print(counter)


"""
nonlocal scope
"""

counter = 0


# def increment():
#     counter = 100
#
#     def inner_increment():
#         # counter = 200
#         nonlocal counter
#         counter += 1
#         print(counter)
#
#     inner_increment()
#
# increment()


"""
Проблема global і валідний варіант

Найкраща функція, яка знає тільки про себе , вона ізольована
"""

counter = 100

def increment(value):
    return value + 1


counter = increment(counter)
print(counter)