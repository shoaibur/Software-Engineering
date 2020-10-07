### Important terms
* General
  * Node and edge
  * Root node and leaf node
  * Neighbor (Parent node and child node)
  * Levels
* Binary tree
  * A node has a maximum of 2 children (left and right)
  * Maximum nodes at level L = 2 ^ L, where L = 0, 1, ... and L = 0 represents the level with root node.
  * Types of binary tree
    * Complete: Each level is complete except the last level. The last level is filled from left to right.
    * Full: Each node has either 0 or 2 children.
    * Perfect: Complete and full. Contains 2^h - 1 nodes, where h is the height of the tree..
    * Balanced: Left height and right height differ by at most 1.
* Binary Search Tree (BST)
  * For all node, left < root < right
* Tree node
```
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
```
* Basic operations
  * Insert (into BST)
    ```
    def insert(root, val):
        if not root: return TreeNode(val)
        
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
            
        return root
    ```
  *  Search (in BST)
    ```
    def search(root, val):
        if not root: return None
        if root.val == val: return root
        
        if val < root.val:
            return search(root.left, val)
        else:
            return search(root.right, val)
    ```
  * Traversal
    * DFS
      * Preorder
      * Inorder
      * Postorder
    * BFS

### Leetcode exeercises on trees
* 297: Serialize and deserialize binary tree
* 199: Binary tree right side view
* 124: Binary tree maximum path sum
* 105: Construct binary tree from preorder and inorder traversal
* 543: Diameter of binary tree
* 987: Vertical order traversal of a binary tree
* 863: All nodes distance K in binary tree
* 98: Validate binary search tree
* 173: Binary search tree iterator
* 236: Lowest common ancestor of a bianry tree
* 103: Binary tree zigzag level order traversal
* 96: Unique binary search tree
* 938: Range sum of BST
* 226: Invert binary tree
* 437: Path sum III
* 102: Binary tree level order traversal 
* 114: Flatten binary tree to linked list
* 101: Symmetric tree
* 104: Maximum depth of binary tree
* 94: Binary tree inorder traversal
* 117: Populating next right pointers in each node II
* 108: Convert sorted array to binary search tree
* 449: Serialize and deserialize BST
* 545: Boundary of binary tree
* 426: Convert binary search tree to sorted doubly linked list
* 113: Path sum II
* 116: Populating next right pointers in each node
* 107: Binary tree level order traversal II
* 112: Path sum
* 270: Closest binary search tree value
* 572: Subtree of another tree
* 617: Merge two binary trees
* 106: Construct binary tree from inorder and postorder traversal
* 257: Binary tree paths
* 662: Maximum width of binary tree
* 1123: Lowest common ancestor of deepest leaves
* 110: Balanced binary tree
* 404: Sum of left leaves
* 285: Inorder successor in BST
* 958: Check completeness of a binary tree
* 145: Binary tree postorder traversal
* 515: Find largest value in each tree row
* 100: Same tree
* 111: Minimum depth of binary tree
* 235: Lowest common ancestor of a binary search tree
* 144: Binary tree preorder traversal
* 865: Samllest subtree with all the deepest nodes
* 700: Search in binary search tree
* 510: Inorder successor in BST II
* 1305: All elements in two binary search trees
* 701: Insert into a binary search tree
* 1022: Sum of root to leaf binary numbers
* 1602: Find nearest right node in binary tree
