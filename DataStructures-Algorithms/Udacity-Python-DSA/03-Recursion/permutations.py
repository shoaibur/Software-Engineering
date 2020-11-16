# Solution 1: iteration
def permutations(string):
    if len(string) <= 1: return string
    out = []
    for i in range(len(string)):
        first = string[i]
        rem = string[:i] + string(i+1:)
        for p in permutations(rem):
            out.append(first + p)
    return out

# Solution 2: backtracking
def permutations(string):
    string = [char for char in string]
    first, last = 0, len(string)-1
    
    def perms(string, first, last):
        if len(string) <= 1: return string
        for i in range(first, last+1):
            string[first], string[i] = string[i], string[first]
            perms(string)
            string[first], string[i] = string[i], string[first]
        return string
    
    return perms(string, first, last)
  
