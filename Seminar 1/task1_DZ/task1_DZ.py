# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:

# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

# def SumDigits(n, res1):
#     # res = 0
#     if n == 0:
#         return
#     else: 
#         res1 += n%10
#         n//10
#         SumDigits(n, res1)


# n =11203351
# res = SumDigits(n)
# print(res)

n=999
n1 = str(n)
n1.split()
res = res1 = 0
while n>0:
    res += n%10
    n//=10
print(res)

for i in range(len(n1)):
    print(n1[i])
    res1+=int(n1[i])
print(res1)
