def power(x, n):
    ntype = ['pos' if n > 0 else 'neg']
    if n == 0: return 1
    n = abs(n)
    xn = x * power(n-1)
    if ntype[0] == 'neg':
        return 1 / xn
    return xn
  
  
def power(x, n):
    ntype = ['pos' if n > 0 else 'neg']
    if n == 0: return 1
    n = abs(n)
    xn = sum( [x]*n )
    if ntype[0] == 'neg':
        return 1 / xn
    return xn
