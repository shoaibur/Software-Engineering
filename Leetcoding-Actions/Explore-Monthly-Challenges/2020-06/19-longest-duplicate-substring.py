# Given a string S, consider all duplicated substrings: (contiguous) substrings of S 
# that occur 2 or more times.  (The occurrences may overlap.)
# Return any duplicated substring that has the longest possible length.  (If S does 
# not have a duplicated substring, the answer is "".)

def longest_dup_substring(S):
    n = len(S)
    d = set()
    maxlen = 0
    longsubstr = ''
    for i in range(n-1):
        for j in range(i+maxlen, n):
            substr = S[i:j+1]
            if substr in d:
                if len(substr) > maxlen:
                    maxlen = len(substr)
                    longsubstr = substr
            else:
                d.add(substr)
    return longsubstr
