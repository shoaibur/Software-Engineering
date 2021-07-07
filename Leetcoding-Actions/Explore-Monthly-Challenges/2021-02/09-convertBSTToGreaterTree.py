# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        '''
        T: O(n) and S: O(n)
        '''
        if not root: return None
        
        nums = []
        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        inorder(root)
        cumsum = [nums[-1]]
        for num in nums[:-1][::-1]:
            cumsum.append(cumsum[-1] + num)
        cumsum[:] = cumsum[::-1]
        print(nums)
        print(cumsum)
        
        d = {}
        for i, num in enumerate(nums):
            d[nums[i]] = cumsum[i]
        
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            curr.val = d[curr.val]
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        
        return root
