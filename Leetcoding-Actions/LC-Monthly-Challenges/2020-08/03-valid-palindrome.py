class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        
        s = s.lower().replace(' ', '')
        for p in string.punctuation:
            s = s.replace(p, '')
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        
        validchar = string.ascii_lowercase + '0123456789'
        i, j = 0, len(s)-1
        while i < j:
            while i < len(s)-1 and s[i].lower() not in validchar:
                i += 1
            while j >= 0 and s[j].lower() not in validchar:
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
            
        return True
