def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
            if len(d) > 4:
                return 0
    return sorted(d)
res = []
for i in range(234432, 234567 + 1):
    if div(i) != 0:
        if len(div(i)) == 4:
            res.append([i, div(i)])
for _ in res:
    print(_)