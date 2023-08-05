a = int(input('first digit '))
b = int(input('second digit '))
print((a>b)) # вариант формирования ответа в бинарном виде True/False
print(((a>b)*10)//10) # вариант формирования ответа в бинарном виде 1/0

if a >b:
    print(f"first = {a} > second = {b}")
elif a == b:
    print(f"first = {a} = second = {b}")
else: print(f"second = {b} > first = {a}")
