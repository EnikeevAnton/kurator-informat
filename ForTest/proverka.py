from functools import *
@lru_cache(None)
def f(n):
    if n == 0: return 1
    if n > 0 and n % 2 != 0:
        return 1 + f(n - 1)
    else:
        return f(n // 2)
for i in range(1, 500_000_001):
    just = f(i)
res = []
for i in range(1, 500_000_001):
    if f(i) == 5:
        res.append(i)
print(res)
