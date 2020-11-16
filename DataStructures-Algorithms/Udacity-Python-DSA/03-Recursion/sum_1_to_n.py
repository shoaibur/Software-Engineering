def sum_1_to_n(n):
    if n <= 1: return n
    return n + sum_1_to_n(n-1)
