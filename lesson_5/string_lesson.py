"""
Функціонал рядку подібний до списку:
- індексація
- присвоєння значення зрізу буде видавати помилку - бо незмінний тип даних
- додавання
- множення
- зрізи
- довжина
- робота через цикл
- оператор in

Прості методи:

- upper()
- lower()
- title()
- capitalize()
- swapcase()
- ljust(), rjust(), center()
- replace()
- split()
- join()
- strip(), lstrip(), rstrip()
- find()
- isalpha()
- isdigit()
-  islower(), isupper(), startswith(), endswith(), istitle()
- zfill() заповнює рядки зліва нулями до вказаної ширини.


Методи рядку та f string

Задачки:
- Порахувати голосні
- Видалити всі пробіли
- text = "   aNnA   " - зробити ім´я в коректному форматі
- Маскування номеру phone = "1234567890" -> "******7890" - replace() , index
- ппорахувати слова text = "I love Python very much" - split()
- перевірити валідність username = "User_123" - дозволені тільки букви та цифри бкз пробілів
- знайти слово в текств text = "I love Python" find()

"""

#Рахуємо голосні

# vowels = 'aeiou'
#
# text = "Hello world"
# result = 0
#
# for letter in text:
#     if letter in vowels:
#         result += 1
#
# print(f'Count of vowels in the {text} is {result}')


# Видаляємо пробіли

# text = "I love Python"
# result = text.replace(' ', '')
# print(result)

# Робимо коректний формат
# text = "   aNnA   "
# test = text.strip().casefold().title()
# print(test)


#Маскування номеру phone = "1234567890"

# phone = "1234567890"
# phone = phone.replace(f"{phone[:6]}", f"{6*'*'}")
# print(phone)
# hided_number = 6 * '*' + phone[6:]
# print(f'{6 * '*'}{ phone[6:]}')

# Перевіряємо валідність username = "User_123"

# username = "User_123"
# result = True
#
# if not username.isalnum():
#     result = False
#
# print(result)

# Знайти слово в тексті text = "I love Python"

# text = "I love Python"
# print(text.find("abc"))




