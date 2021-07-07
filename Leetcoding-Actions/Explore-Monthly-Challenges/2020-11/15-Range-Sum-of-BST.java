/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        /**
        * T: O(n) and S: O(n)
        */
        if (root == null) return 0;
        
        int sum = 0;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        
        while (true) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            if (stack.isEmpty()) break;
            
            curr = stack.pop();
            
            if (curr.val >= low && curr.val <= high) {
                sum += curr.val;
            }
            if (curr.val > high) {
                return sum;
            }
            
            curr = curr.right;
        }
        return sum;
    }
}
