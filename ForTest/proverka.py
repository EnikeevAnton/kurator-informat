def f(c,m,t):
    if c>=78: return m%2 == 0
    if m == 0: return 0
    h = [f(c+1,m-1,t + 1), f(c+4, m - 1, t + 1), f(c*4, m - 1, t + 1)]
    return any(h) if m%2 !=0 else all(h)
#print('19', [s for s in range(1,78) if f(s, 2, [])])
print([s for s in range(1,78) if f(s,9, 0) and not f(s, 7, 0)])