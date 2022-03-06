# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = {}
        
        
        def dfs(root):
            if not root:
                return 0
            #print(root.val)
            if root in dp:
                return dp[root]
            choose = root.val
            if root.left:
                if root.left.left:
                    choose += dfs(root.left.left)

                if root.left.right:
                    choose += dfs(root.left.right)
                    
            if root.right:
                if root.right.left:
                    choose+=  dfs(root.right.left) 

                if root.right.right:
                    choose += dfs(root.right.right)
            
            notChoose = dfs(root.right) + dfs(root.left)
            
            dp[root] = max(choose,notChoose)
            return dp[root]
        
        
        return dfs(root)
        
        