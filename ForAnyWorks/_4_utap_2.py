from itertools import permutations
def prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
res = 0
for i in permutations('0123456789', r = 6):
    if i[0] != '0':
        s = int(''.join(i))
        s1 = s // 100_000
        s2 = s % 100_000 // 10_000
        s3 = s % 10_000 // 1000
        s4 = s % 1000 // 100
        s5 = s % 100 // 10
        s6 = s % 10
        if s1 % 2 == s6 % 2:
            if prime(s):
                if s2 % 3 == s5 % 3:
                    if s3 + s4 < s1 + s6:
                        res += 1
print(2112 - res)


