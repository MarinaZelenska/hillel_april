"""
Умовні оператори в Python (if, elif, else)
"""
# Task 1
age = 16

if age >= 18:
    print('Доступ дозволено')
else:
    print('Доступ заборонено')

# Task 2

score = 75

if score >= 90:
    print('Відмінно')
elif score >= 70:
    print('Добре')
elif score >= 50:
    print('Задовільно')
else:
    print('Не склав')

# TASK 3

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print('Вхід дозволено')
    else:
        print('Потрібен квиток')
else:
    print('Ти занадто молодий')



"""
Тернарний оператор
"""


age = 20

result = 'Дорослий' if age >= 18 else 'Дитина'
print(result)

# Task

hour = 8

if 0 > hour > 24:
    print("Invalid hour")
elif hour > 22:
    print("Good night")
elif 10 >= hour >= 6:
    print("Good morning")
elif 17 >= hour > 10:
    print("Good afternoon")
else:
    print("Good evening")