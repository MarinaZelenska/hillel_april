"""
tuple
<class 'tuple'>


immutable data types
int
float
bool
str
tuple

mutable data types
list
dict -> key value pair

"""



it_department = [
    {"name": "Anna", "age": 25},
    {"name": "John", "age": 30},
    {"name": "John 2", "age": 45},
    {"name": "John 3", "age": 10},
]




for item in it_department:
    if item['age'] > 26:
        print(item)


