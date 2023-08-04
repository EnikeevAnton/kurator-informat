def f(x, y, a):
    return ((2 * x) + (3 * y) > 30) or (x + y <= a)

for a in range(0, 100):
    if all(f(x, y, a) == 1 for x in range(0, 100) for y in range(0, 100)):
        print(a)
        break
