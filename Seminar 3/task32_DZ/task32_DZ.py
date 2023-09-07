# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def elements_inrange(arr, minimum, maximum):
    res=[]
    for i in range(n):
        if arr[i] > minimum and arr[i] < maximum:
            res.append(i)
    return res

n = int(input("Укажите размер массива: "))
arr = [int(input(f"введите число {i} из {n}: ")) for i in range(1, n+1)]
min_arr = int(input("Укажите мин. значение: "))
max_arr = int(input("Укажите макс. значение: "))
result = elements_inrange(arr, min_arr, max_arr)
print(f"Массив: {arr}")
print(f"Индексы элементов массива, значения которых больше {min_arr} и меньше {max_arr}: {result}")