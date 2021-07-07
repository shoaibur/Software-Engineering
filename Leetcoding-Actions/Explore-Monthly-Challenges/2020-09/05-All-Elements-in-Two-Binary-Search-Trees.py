# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorderTraverse(root):
            nums = []
            def inorder(root):
                if root:
                    inorder(root.left)
                    nums.append(root.val)
                    inorder(root.right)
            inorder(root)
            return nums
        
        nums1 = inorderTraverse(root1)
        nums2 = inorderTraverse(root2)
        
        def merge(nums1, nums2):
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
        return merge(nums1, nums2)
