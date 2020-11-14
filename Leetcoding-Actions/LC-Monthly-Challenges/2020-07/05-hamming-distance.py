def hammingDistance(x, y):
    z = str( bin(x ^ y) )
    return sum( [int(i) for i in z if i == '1'] )
