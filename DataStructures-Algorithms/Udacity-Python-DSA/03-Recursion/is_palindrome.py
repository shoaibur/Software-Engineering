def reverse(string):
    #return string[::-1]
    if len(string) <= 1: return string
    return string[-1] + reverse(string[:-1])
  
def is_palindrome(string):
    if string != reverse(string):
        return False
    return True
  
def is_palindrome2(string):
    i, j = 0, len(string)-1
    while i < j:
        if string[i] != string[j]:
            return False
    return True
