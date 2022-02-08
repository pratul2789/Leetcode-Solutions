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

import java.util.*;

class Solution {
    
    public boolean helper(TreeNode node1, TreeNode node2){
        if(node1 == null && node2 == null){
            return true;
        }
        
        if(node1 == null || node2 == null){
            return false;
        }
        
        if(node1.val != node2.val){
            return false;
        }
        
        return helper(node1.right,node2.left) && helper(node1.left,node2.right);
    }
    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        
        return helper(root.left,root.right);
    }
}