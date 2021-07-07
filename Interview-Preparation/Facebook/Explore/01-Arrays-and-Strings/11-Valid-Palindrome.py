import string
letters = string.ascii_lowercase + string.ascii_uppercase
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        for punc in string.punctuation:
            s = s.replace(punc, '')
        print(s)
        i, j = 0, len(s)-1
        while i < j:
            # if s[i] not in letters:
            #     i += 1
            # if s[j] not in letters:
            #     j -= 1
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True
    
