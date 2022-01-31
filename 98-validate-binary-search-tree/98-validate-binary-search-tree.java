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
    List<Integer> res = new ArrayList<Integer>();

    public void inorder(TreeNode root){
        if(root != null){
            // Start exploring the left child
            inorder(root.left);
            res.add(root.val);
            // Start exploring the right child
            inorder(root.right);
        }
    }

    public boolean isValidBST(TreeNode root) {
        inorder(root);

	// Check if the list is sorted or not
	    for(int i = 0; i < res.size()-1; i++){
		// At any point if we find a breach, then we know it is not in a sorted order
		if(res.get(i) >= res.get(i+1)){
			return false;
            }
        }
        
        return true;
}
}