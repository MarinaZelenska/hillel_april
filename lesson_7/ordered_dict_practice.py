from collections import OrderedDict


fruits = OrderedDict({
    "apple": 10,
    "banana": 20,
    "orange": 30
})

# fruits.move_to_end('orange', last=False)
# print(fruits)
fruits.popitem(last=False)
print(fruits)