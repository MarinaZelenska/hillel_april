"""
Цикл for використовується для перебору елементів
(списків, рядків, чисел через range і т.д.)
Синтаксис:
for елемент in колекція:
    код
"""


# 1. Найпростіший приклад

numbers = [1, 2, 3, 4, 5]

for element in numbers:
    print(element)


# 2. Робота з числами (range)


# range(5) -> 0,1,2,3,4
for i in range(5):
    print(i)


# range(start, stop)
for i in range(2, 6):
    print(i)


# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)


# 3. Сума чисел у списку

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

print("Сума:", total)



# 4. Пошук максимального числа


numbers = [3, 7, 2, 9, 5]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Максимум:", max_num)




# --------------------------------------
# 6. Парні та непарні числа
# --------------------------------------

for i in range(10):
    if i % 2 == 0:
        print(i, "парне")
    else:
        print(i, "непарне")


# --------------------------------------
# 7. Робота зі списками (фільтрація)
# --------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Парні числа:", even_numbers)


# --------------------------------------
# 8. enumerate() — індекс + значення
# --------------------------------------

names = ["Anna", "Ivan", "Oleg"]

for index, name in enumerate(names):
    print(index, name)


# --------------------------------------
# 9. zip() — об'єднання списків
# --------------------------------------

names = ["Anna", "Ivan"]
ages = [20, 25]

for name, age in zip(names, ages):
    print(name, age)



# --------------------------------------
# 10. break — зупинка циклу
# --------------------------------------

for i in range(10):
    if i == 5:
        break
    print(i)


# --------------------------------------
# 11. continue — пропустити ітерацію
# --------------------------------------

for i in range(5):
    if i == 2:
        continue
    print(i)
