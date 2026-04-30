"""
Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

Декілька правил:

ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
підсумкова довжина hashtag має бути не більше 140 символів.
кожне слово починається з великої літери.
якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
'Python Community' -> #PythonCommunity
'i like python community!' -> #ILikePythonCommunity
'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

"""
# import string
# custom_str = 'Should'.title()
# hashtag = ''
#
# for letter in custom_str:
#     if letter not in string.punctuation and not letter.isspace():
#         hashtag += letter
#
# hashtag = f'#{hashtag}'[:140]


"""
Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.

Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.

Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA

"""
#
# from string import ascii_letters
#
# user_input = input("Enter your letter: ")
#
# index_first, index_second = ascii_letters.index(user_input[0]), ascii_letters.index(user_input[-1])
# result = ascii_letters[index_first: index_second + 1]


"""
Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
Користувач вводить число з клавіатури.

999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
1000 -> 0
423 -> 8
33 -> 9
25 -> 0
1 -> 1

"""

# number = int(input("Enter a number: "))
#
# while number > 9:
#     result = 1
#     for el in str(number):
#         result *= int(el)
#     number = result
#
# print(number)

"""
Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.

Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.

Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.

Ну і додатковим завданням є турбота про виведення.

Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.

Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек. Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)

Доповнити провідними нулями можна за допомогою методу zfill(2)


0 -> 0 днів, 00:00:00
224930 -> 2 дні, 14:28:50
466289 -> 5 днів, 09:31:29
950400 -> 11 днів, 00:00:00
1209600 -> 14 днів, 00:00:00
1900800 - > 22 дні, 00:00:00
8639999 -> 99 днів, 23:59:59
22493 -> 0 днів, 06:14:53
7948799 -> 91 день, 23:59:59

"""

# number = int(input("Enter number: "))
# endings = 'днів'
#
# if 0 <= number < 8640000:
#     days, remaining = divmod(number, 86400)
#     hours, remaining = divmod(remaining, 3600)
#     minutes, seconds =  divmod(remaining, 60)
#
#
# if days % 10 == 1:
#     endings = 'день'
# elif 2 <= days % 10 <= 4:
#     endings = 'дні'
# else:
#     endings = 'днів'
#
# print(f'{days} {endings}, {hours:02}:{minutes:02}:{seconds:02}')
#

# from string import ascii_letters
# while True:
#  string_1 = input("Введiть двi лiтери через дефiс: ")
#  start_str, end_str = string_1.split('-')
#  start_pos, end_pos = ascii_letters.find(start_str), ascii_letters.find(end_str)
#  print(ascii_letters[start_pos:end_pos + 1] )
#  user = input("Продовжити: Y/N")
#  if user == "Y":
#      continue
#  if user == "N":
#     print("Робота завершена")
#     break


def multiply_digits(n):
    if n <= 9:
        return n
    product = 1
    for digit in str(n):
        product *= int(digit)
    return multiply_digits(product)

n = int(input().strip())
print(multiply_digits(n))