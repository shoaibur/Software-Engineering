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
    private int totalTilt = 0;
    
    public int findTilt(TreeNode root) {
        tiltSum(root);
        return totalTilt;
    }
    
    protected int tiltSum(TreeNode root) {
        if (root == null) return 0;
        
        int leftSum = tiltSum(root.left);
        int rightSum = tiltSum(root.right);
        int tilt = Math.abs(leftSum - rightSum);
        totalTilt += tilt;
        
        return leftSum + rightSum + root.val;
    }
}
