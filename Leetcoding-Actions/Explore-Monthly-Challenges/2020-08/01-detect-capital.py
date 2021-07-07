class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # d={}
        # for accii in range( ord('A'), ord('Z')+1 ):
        #     d[chr(accii)] = accii
        return word.isupper() or word.istitle() or word.islower()
