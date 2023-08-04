def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sum(d)
res = []
second = []
for x in range(89031860601, 89031869692):
    if x%27 == 0:
        ch = str(x)
        if len(ch) == 11 and ch[-1] == '1':
            if ch[0:7] == '8903186' and ch[-3] == '6':
                res.append(x + div(x))
                second.append(x + x//27)
print(res, "ответ, если необходимо сложить число со всеми его делителями \n", second, 'ответ, если необходимо сложить число с резульатом деления этого числа на 27')