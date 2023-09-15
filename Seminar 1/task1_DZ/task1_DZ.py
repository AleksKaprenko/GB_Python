# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:

# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

# Var 1
def SumDigits(n, summ):
    if n == 0:
        return summ
    else: 
        summ += n%10
        return SumDigits(n//10, summ)

num =123123123
res = SumDigits(num, 0)
print(res)


# Var 2
n=999
res = 0
while n>0:
    res += n%10
    n//=10
print(res)

# Var 3

n=999
n1 = str(n)
n1.split()
res = 0
for i in range(len(n1)):
    res += int(n1[i])
print(res)
