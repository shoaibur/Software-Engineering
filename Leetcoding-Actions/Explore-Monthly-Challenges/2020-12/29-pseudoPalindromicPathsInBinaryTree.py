# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        def isPalindrome(path):
            d = {}
            for digit in path:
                d[digit] = d.get(digit, 0) + 1            
            evenCount = 0
            for digit in d:
                evenCount += d[digit] % 2
                if evenCount > 1:
                    return False
            return True
        
        panlindromPathCount = 0
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                if isPalindrome(path):
                    panlindromPathCount += 1
            if node.left:
                stack.append((node.left, path + [node.left.val]))
            if node.right:
                stack.append((node.right, path + [node.right.val]))
        return panlindromPathCount
