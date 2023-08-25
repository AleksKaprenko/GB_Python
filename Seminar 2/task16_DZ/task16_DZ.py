# найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6 -> 5

list_1 = [1, 2, 3, 4, 5]
k = 6
min_distance = abs(k-list_1[0])
index = 0
for i in range(1, len(list_1)):
    temp = abs(k-list_1[i])
    if min_distance > temp: # если > - в результат попадает первый найденный эл-т, если >= то последний найденный
        min_distance = temp
        index = i
print(list_1[index])
    