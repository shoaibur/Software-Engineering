class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictS = {}
        for char in s:
            dictS[char] = dictS.get(char, 0) + 1
        
        for char in t:
            if char in dictS:
                dictS[char] -= 1
                if dictS[char] == 0:
                    dictS.pop(char)
            else:
                return char
        return None
