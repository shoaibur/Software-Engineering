# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

def reverse_string(s):
    if len(s) <= 1: return s
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i, j = i + 1, j - 1
    return s
