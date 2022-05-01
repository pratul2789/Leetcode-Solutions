# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        def dfs(root,parVal):
            
            if not root:
                return parVal
            
            
            right  = dfs(root.right,parVal)
            root.val = right + root.val
            left = dfs(root.left,root.val)
            
            return left
        
        dfs(root,0)
        return root
        