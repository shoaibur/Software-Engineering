def dfs_inorder(tree):
    if tree is None: return None
    out = []
    dfs_inorder(tree.left)
    out.append(tree.value)
    print(tree.value)
    dfs_inorder(tree.right)
    return out
    
def dfs_preorder(tree):
    if tree is None: return None
    out = []
    out.append(tree.value)
    print(tree.value)
    dfs_preorder(tree.left)
    dfs_preorder(tree.right)
    return out
    
def dfs_postorder(tree):
    if tree is None: return None
    out = []
    dfs_postorder(tree.left)
    dfs_postorder(tree.right)
    out.append(tree.value)
    print(tree.value)
    return out
