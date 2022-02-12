# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        
        def dfs(root):
            if not root:
                return root
            
            if low <= root.val <= high:
                root.left = dfs(root.left)
                root.right = dfs(root.right)
            elif root.val < low:
                root = dfs(root.right)
            elif root.val > high:
                root = dfs(root.left)
                
            return root
        
        return dfs(root)