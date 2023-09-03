a = {2, 5, 12, 17, 7, 22, 10, 1}
b = {17, 10, 8, 1, 77}
res = list()
for i in a:
    if i in b:
        res.append(i)
res.sort()
print(res)
