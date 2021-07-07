# Posible steps: 1 or 2
# n=1 --> 1 --> 1
# n=2 --> 11, 2 --> 2
# n=3 --> 111, 12, 21 --> 3
# n=4 --> 1111, 112, 121, 211, 22 --> 5
# f[n] = f[n-1] + f[n-2]

def staircase(n):
    if n <= 2: return n
    return staircase(n-1) + staircase(n-2)
  
def staircase(n):
    if n <= 2: return n
    a, b = 1, 2
    for i in range(3, n+1):
        out = a + b
        a, b = b, out
    return out
  
# Possible steps: 1 or 2 or 3
# n=1 --> 1 --> 1
# n=2 --> 11, 2 --> 2
# n=3 --> 111, 12, 21, 3 --> 4
# n=4 --> 1111, 112, 121, 211, 22, 13, 31 --> 7
# n=5 --> 11111, 1112, 1121, 1211, 2111, 221, 122, 212, 113, 131, 311, 32, 23 --> 13
# f[n] = f[n-1] + f[n-2] + f[n-3]

def staircase(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return staircase(n-1) + staircase(n-2) + staircase(n-3)

def staircase(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    a, b, c = 1, 2, 4
    for i in range(4, n+1):
        out = a + b + c
        a, b, c = b, c, out
    return out
