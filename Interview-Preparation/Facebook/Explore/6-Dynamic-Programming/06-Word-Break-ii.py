def wordBreak(s, wordDict):
    dp = {}
    def word_break(s):
        if s in dp: return dp[s]
        words = []
        for word in wordDict:
            if word == s[:len(word)]:
                if len(word) == len(s):
                    words.append(word)
                else:
                    temp = word_break(s[len(word):])
                    for t in temp:
                        words.append(word + ' ' + t)
        dp[s] = words
        return words
    return word_break(s)
