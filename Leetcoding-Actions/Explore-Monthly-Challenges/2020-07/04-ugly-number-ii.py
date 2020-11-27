def nthUglyNumber(n):
    ugly = [1]
    count = 1
    idx2, idx3, idx5 = 0, 0, 0
    while count < n:
        next2 = ugly[idx2] * 2
        next3 = ugly[idx3] * 3
        next5 = ugly[idx5] * 5
        
        nextt = min(next2, next3, next5)
        ugly.append(nextt)
        count += 1
        
        if nextt == next2: idx2 += 1
        if nextt == next3: idx3 += 1
        if nextt == next5: idx5 += 1
    return ugly[-1]
