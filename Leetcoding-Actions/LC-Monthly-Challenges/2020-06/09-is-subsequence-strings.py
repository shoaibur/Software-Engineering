# Given a string s and a string t, check if s is subsequence of t.
# A subsequence of a string is a new string which is formed from the original string by deleting 
# some (can be none) of the characters without disturbing the relative positions of the remaining 
# characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
