# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        
        
        def dfs(node, low, high):
            if node:
                total = 0
                if low <= node.val <= high:
                    total += node.val
                    
                if low  < node.val:
                    total += dfs(node.left, low, high)
                    
                if high > node.val:
                    total += dfs(node.right, low, high)
                
                return total
            else:
                return 0
            
        return dfs(root, low, high)