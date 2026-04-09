"""
ЛЕКЦІЯ: Булевий тип даних у Python

Булевий тип даних (bool) — це тип, який має лише 2 значення:
True  - істина
False - хиба
"""

first = True
second = False
# print(first)
# print(second)

#  bool похідний від int
# print(int(first))
# print(int(second))

# можна навпаки int перевести в bool

int_to_bool_true = bool(1)
int_to_bool_false = bool(0)
test = bool(10)
# print(int_to_bool_true)
# print(int_to_bool_false)
# print(test) # все що не 0 буде True

"""
ОПЕРАТОРИ ПОРІВНЯННЯ
 ==   дорівнює
 !=   не дорівнює
 >    більше
 <    менше
 >=   більше або дорівнює
 <=   менше або дорівнює
"""

x = 10
y = 15
# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)


"""
BOOL У ЗМІННИХ
"""
age = 20
is_adult = age >= 18
print(is_adult)

temperature = 37.5
has_fever = temperature > 36.6
print(has_fever)

"""
ЛОГІЧНІ ОПЕРАТОРИ: and, or, not
"""

age = 25
has_ticket = True

print(age >= 18 and has_ticket)
print(age < 18 or has_ticket)
print(not has_ticket)

login = 'admin'
password = '12345'

print(login == 'admin' and password == '12345')
print(login == 'user' and password == '12345')

number = 12
print(number > 0 and number % 2 == 0)


day = 'Saturday'
print(day == 'Saturday' or day == 'Sunday')

user_role = 'moderator'
print(user_role == 'admin' or user_role == 'moderator')


is_raining = False
print(not is_raining)

is_logged_in = True
print(not is_logged_in)