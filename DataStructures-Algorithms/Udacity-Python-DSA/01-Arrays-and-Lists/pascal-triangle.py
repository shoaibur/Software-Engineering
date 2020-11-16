#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

def pascal_triangle(n):
    if n == 1: return n
    out = [1, 1]
    for i in range(3, n+1):
        b = []
        for j in range(len(out)-1):
            b.append(out[j]+out[j+1])
        out = [1] + b + [1]
    return out
