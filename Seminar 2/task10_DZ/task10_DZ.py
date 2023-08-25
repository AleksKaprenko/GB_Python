# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# Решение:
# Создадим список размера n с произвольным набором 1 (решка = avers) и 0 (герб = reverse)
# Выполним подсчет количества 1 и 0 в списке и выведем меньшее из них


import random

n=int(input("Число монет на столе: "))
arr = []
count_avers = count_revers = 0

for i in range(n-1):
    arr.append(random.randint(0, 1)) # заполнение списка произвольным набором 1 и 0
    
for i in range(len(arr)):
    if arr[i]==1: count_avers+=1
    else: count_revers +=1

print(arr) 

# variant 1
# if  count_avers >= count_revers: print(f"{count_revers}")
# else: print(f"{count_avers}")

# variant 2
print("Мин. количество монет для преворота: ", [count_avers, count_revers][count_avers >= count_revers])


