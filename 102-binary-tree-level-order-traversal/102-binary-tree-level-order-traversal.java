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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(root == null) return result;
        
        Deque<TreeNode> q = new LinkedList<>();
        
        q.add(root);
        
        while(q.isEmpty() != true){
            int nodeToProcess = q.size();
            List<Integer> l1 = new ArrayList<>();
            
            for(int i = 0; i < nodeToProcess; i++){
                TreeNode node = q.pollFirst();
                l1.add(node.val);
                
                if(node.left != null){
                    q.add(node.left);
                }
                
                if(node.right != null){
                    q.add(node.right);
                }
            }
            
            result.add(l1);
        }
        
        return result;
    }
}