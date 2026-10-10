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
    private boolean balanced = true;
    public boolean isBalanced(TreeNode root) {
        traverseHeight(root);
        return balanced;
    }
    public int traverseHeight(TreeNode root){
        if(balanced == false){
            return 0;
        }
        if(root == null){
            return 0;
        }
        int left = traverseHeight(root.left);
        int right = traverseHeight(root.right);
        if(left - right > 1 || left - right < -1){
            balanced = false;
        }
        return Math.max(left, right) + 1;
    }
}
