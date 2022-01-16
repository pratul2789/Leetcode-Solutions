# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,lower = float('-inf'),upper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not helper(node.right,node.val,upper) or not helper(node.left,lower,node.val): 
                return False
           
            
            return True
        
        
        return(helper(root))