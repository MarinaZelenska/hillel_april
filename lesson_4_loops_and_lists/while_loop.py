"""==

while — це уикл, який виконується поки умова істина (True)

Синтаксис:
while мова:
    код

========================================
"""

i = 0
while i < 5:
    print(i)
    i += 1

print("\n=== 2. БЕСКОНЕЧНЫЙ ЦИКЛ (пример) ===")

# ❗ НЕ ЗАПУСКАЙ без break
# while True:
#     print("Это бесконечный цикл")


print("\n=== 3. BREAK — выход из цикла ===")

i = 0
while True:
    if i == 5:
        break
    print(i)
    i += 1

print("\n=== 4. CONTINUE — пропуск итерации ===")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("\n=== 5. ВВОД ПОЛЬЗОВАТЕЛЯ ===")

# password = ""
# while password != "1234":
#     password = input("Введите пароль: ")
# print("Доступ разрешен")



i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Цикл завершился без break")


import random

status = 500

while status != 200:
    status = random.choice([200, 500])
    print(f"Статус: {status}")

print("Успешный ответ получен!")

print("\n=== 10. МИНИ-ИГРА ===")

# import random
# secret = random.randint(1, 10)
# guess = None
#
# while guess != secret:
#     guess = int(input("Угадай число от 1 до 10: "))
#
#     if guess < secret:
#         print("Больше")
#     elif guess > secret:
#         print("Меньше")
#
# print("Ты угадал 🎉")


print("\n=== 11. ТИПИЧНЫЕ ОШИБКИ ===")

# ❌ Ошибка 1: бесконечный цикл
# i = 0
# while i < 5:
#     print(i)  # нет i += 1

# ❌ Ошибка 2: условие никогда не выполнится
# i = 0
# while i > 5:
#     print(i)


print("\n=== 12. ПРАКТИКА ===")

print("""
Задания:
1. Вывести числа от 10 до 1 через while
2. Считать сумму чисел, пока пользователь не введет 0
3. Найти первое число > 100, которое делится на 7
""")

print("\n=== КОНЕЦ ЛЕКЦИИ ===")