# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

n=int(input("Введите число N: "))
degree = 0
i = 0
result=[]
while degree <= n:
    degree=2**i
    i+=1
    if degree <=n : result.append(degree)
print (result)