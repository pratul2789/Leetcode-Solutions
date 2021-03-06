# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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