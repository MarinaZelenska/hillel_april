
number = 57

num_1, num_2 = divmod(number, 2)
print(num_1, num_2)  # 28 1
num_3, num_4 = divmod(num_1, 2)
print(num_3, num_4)  # 14 0
num_5, num_6 = divmod(num_3, 2)
print(num_5, num_6) # 7 0
num_7, num_8 = divmod(num_5, 2)
print(num_7, num_8) # 3 1
num_9, num_10 = divmod(num_7, 2)
print(num_9, num_10) # 1 1
num_11, num_12 = divmod(num_9, 2)
print(num_11, num_12) # 0 1

result = '111001'
result_bin = oct(number)
print(result_bin)