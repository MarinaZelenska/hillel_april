"""
ЛЕКЦІЯ: Списки (list) у Python
"""
# Створення списоку

test = list()
test_2 = []

numbers = [1, 2, 3, 4]
names = ['Anna', 'Oleg', 'Marina']
mixed = [1, 'text', True, 3.14]
#
# print(numbers)
# print(names)
# print(mixed)
# print(type(numbers))

# Доступ до елементів

fruits = ['apple', 'banana', 'orange']

print(fruits[0])
print(fruits[1])
print(fruits[-1])


# Додавання елементів

fruits.append('grape')
print(fruits)

fruits.insert(1, 'kiwi')
print(fruits)

# видалення елементів

numbers = [1, 2, 3, 4, 5]

numbers.remove(3)
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(0)
print(numbers)


# перевірка входження

fruits = ['apple', 'banana', 'orange']

print('apple' in fruits)
print('kiwi' in fruits)

if 'papaya' not in fruits:
    fruits.append('papaya')


# розмір списку


numbers = [10, 20, 30, 40]
print(len(numbers))

# складання списку

list1 = [1, 2]
list2 = [3, 4]

result = list1 + list2
print(result)


# збільшення списку на число

nums = [1, 2]
print(nums * 3)


# зрізи

numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::-1])  # реверс


# ============================================================
# 10. ПРАКТИЧНІ ПРИКЛАДИ
# ============================================================
print('\n--- 10. Практика ---')

# перевірка кошика
cart = ['milk', 'bread']
if cart:
    print('Є товари')

# додати товар
cart.append('apple')
print(cart)

# перевірка товару
print('milk' in cart)


# ============================================================
# 11. ТИПОВІ ПОМИЛКИ
# ============================================================
print('\n--- 11. Помилки ---')

# ❌ fruits[10] -> IndexError

# ❌ remove якщо елементу немає


# ============================================================
# 12. ЗАВДАННЯ
# ============================================================
# 1. Створи список з 5 чисел
# 2. Додай ще одне число
# 3. Видали другий елемент
# 4. Перевір чи є число 10
# 5. Виведи довжину списку


# ============================================================
# 13. ВІДПОВІДІ
# ============================================================
print('\n--- 13. Відповіді ---')

nums = [1, 2, 3, 4, 5]
nums.append(6)
nums.pop(1)
print(10 in nums)
print(len(nums))

