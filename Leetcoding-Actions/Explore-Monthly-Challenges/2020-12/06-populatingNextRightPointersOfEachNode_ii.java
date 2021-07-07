/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null) return root;
        
        ArrayDeque<Node> q = new ArrayDeque<>();
        q.addLast(root);
        
        while (!q.isEmpty()) {
            int size = q.size();
            int count = 0;
            Node prevNode = null;
            while (count < size) {
                Node currNode = q.removeFirst();
                
                if (prevNode == null) {
                    prevNode = currNode;
                } else {
                    prevNode.next = currNode;
                    prevNode = currNode;
                }
                
                if (currNode.left != null) {
                    q.addLast(currNode.left);
                }
                if (currNode.right != null) {
                    q.addLast(currNode.right);
                }
                count++;
            }
        }
        return root;
    }
}
