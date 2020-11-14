class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        def word_break(s):
            if s in dp: return dp[s]
            result = []
            for word in wordDict:
                if word == s[:len(word)]:
                    if len(word) == len(s):
                        result.append(word)
                    else:
                        temp = word_break(s[len(word):])
                        for t in temp:
                            result.append(word + ' ' + t)
            dp[s] = result
            return result
        return word_break(s)
