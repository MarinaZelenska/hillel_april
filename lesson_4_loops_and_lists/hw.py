"""
Ваша програма має перенести останній елемент списку з кінця на початок, тобто, останній елемент списку має стати першим.
Послідовність інших елементів не має змінюватися.
"""
#
# custom_list = input("Enter a list of numbers_test using comma and space: ").split(', ')
# last_element = custom_list.pop()
# custom_list.insert(0, last_element)
# custom_list[0] = last_element
# print(custom_list)


"""
[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
[1, 2, 3] => [[1, 2], [3]]
[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
[1] => [[1], []]
[] => [[], []]
"""
custom_list = []
list_len = len(custom_list)
half = list_len // 2
if list_len % 2 == 0 and list_len > 1:
    result = [custom_list[:half], custom_list[half:]]
else:
    result = [custom_list[:half + 1], custom_list[half + 1:]]
print(result)

