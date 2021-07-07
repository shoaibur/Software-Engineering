# Solution 1
def longestValidParentheses(s):
    maxLen = 0
    stack = [-1] # imagine first invalid close at -1
    for i,char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i) # next invalid close
            else:
                maxLen = max(maxLen, i - stack[-1])
    return maxLen


# Solution 2
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        def merge(nums1, nums2): # T: O(n)
            nums = []
            n1, n2 = len(nums1), len(nums2)
            i, j = 0, 0
            while i < n1 or j < n2:
                v1 = nums1[i] if i < n1 else float('inf')
                v2 = nums2[j] if j < n2 else float('inf')
                if v1 < v2:
                    nums.append(v1)
                    i += 1
                else:
                    nums.append(v2)
                    j += 1
            return nums
        
        invalidOpen = []
        invalidClose = []
        
        for i in range(len(s)): # T: O(n)
            if s[i] == '(':
                invalidOpen.append(i)
            else:
                if not invalidOpen:
                    invalidClose.append(i)
                else:
                    invalidOpen.pop()
        invalid = [-1] + merge(invalidOpen, invalidClose) + [len(s)]
        
        maxLen = 0
        for i in range(1, len(invalid)):
            maxLen = max(maxLen, invalid[i] - invalid[i-1] - 1)
        return maxLen
