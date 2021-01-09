class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return ''.join(word1) == ''.join(word2)
        i, j = 0, 0
        w1, w2 = word1[i], word2[j]
        while i < len(word1) and j < len(word2):
            n1, n2 = len(w1), len(w2)
            if n1 == n2:
                if w1 != w2:
                    return False
                i, j = i + 1, j + 1
                w1 = word1[i] if i < len(word1) else ''
                w2 = word2[j] if j < len(word2) else ''
            elif n1 < n2:
                if w1 != w2[:n1]:
                    return False
                i += 1
                w1 = word1[i] if i < len(word1) else ''
                w2 = w2[n1:]
            else:
                if w1[:n2] != w2:
                    return False
                j += 1
                w1 = w1[n2:]
                w2 = word2[j] if j < len(word2) else ''
        return i == len(word1) and j == len(word2)
