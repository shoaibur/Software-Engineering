def sorted_array_bst(nums):
    if not nums: return Node(None)
    mid = len(nums) // 2
    tree = Node( nums[mid] )
    left = nums[:mid]
    right = nums[mid+1:]
    tree.left = sorted_array_bst(left)
    tree.right = sorted_array_bst(right)
    return tree
    
