def insert(tree, value):
    if tree is None: return Node(value)
    if value < tree.value:
        if tree.left is None:
            tree.left = Node(value)
        else:
            insert(tree.left, value)
    else:
        if tree.right is None:
            tree.right = Node(value)
        else:
            insert(tree.right, value)
    return tree
    
def search(tree, value):
    if tree is None: return False
    if value == tree.value: return True
    if value < tree.value:
        return search(tree.left, value)
    else:
        return search(tree.right, value)
    return False

def delete(tree, value):
    if tree is None: 
        return tree  
    if value < tree.value: 
        tree.left = delete(tree.left, value) 
    elif(value > tree.value): 
        tree.right = delete(tree.right, value)   
    # If value is same as tree's value, then this is the node to be deleted 
    else: 
        # Node with only one child or no child 
        if tree.left is None : 
            temp = tree.right  
            tree = None 
            return temp  
        elif tree.right is None : 
            temp = tree.left  
            tree = None
            return temp 
        # Node with two children: Get the inorder successor (smallest in the right subtree) 
        temp = minValueNode(tree.right) 
        # Copy the inorder successor's content to this node 
        tree.value = temp.value 
        # Delete the inorder successor 
        tree.right = deleteNode(tree.right , temp.value) 
    return tree 
