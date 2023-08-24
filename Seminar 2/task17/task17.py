# Задача No17.
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

arr = [1, 1, 2, 0, -1, 3, 4, 4]
new_arr = {}

# var 1
for item in arr:
    if item not in new_arr:
        new_arr[item] = item
print(len(new_arr))
# var 2
print(len(set(arr))) # решение в одну строку, set создвет словарь уникальных элементов