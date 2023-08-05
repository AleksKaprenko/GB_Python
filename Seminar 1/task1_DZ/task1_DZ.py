# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:

# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

# def SumDigits(n):
#     # res = 0
#     # print(n)
#     if n == 0: return
#     res += n%10
#     print(res)
#     SumDigits(n//10)


# n =11203351
# res = SumDigits(n)
# print(res)

n=999
res = 0
while n>0:
    res += n%10
    n//=10
print(res)
