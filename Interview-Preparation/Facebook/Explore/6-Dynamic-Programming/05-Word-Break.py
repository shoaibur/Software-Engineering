def wordBreak(s, wordDict):
    wordDict = set(wordDict)
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1,len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]

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
    return len(word_break(s)) > 0
