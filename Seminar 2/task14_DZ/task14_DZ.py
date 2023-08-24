# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

n=int(input("Введите число N: "))
degree = 1
i = 1
result=[]
while degree <= n:
    result.append(degree)
    degree=2**i
    i+=1
print (result)