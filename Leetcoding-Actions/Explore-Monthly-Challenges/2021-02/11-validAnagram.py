class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)
        
        # d = {}
        # for char in s:
        #     d[char] = d.get(char, 0) + 1
        # for char in t:
        #     if char in d:
        #         d[char] -= 1
        #         if d[char] == 0:
        #             d.pop(char)
        #     else:
        #         return False
        # return True
        
        # count_s = [0] * 26
        # for char in s:
        #     count_s[ord(char)-ord('a')] += 1
        # count_t = [0] * 26
        # for char in t:
        #     count_t[ord(char)-ord('a')] += 1
        # return count_s == count_t
