# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        
        self.ans = 0
        def dfs(root):
            #global ans
            if not root:
                return (0,0)
            
            lcount,lsum = dfs(root.left)
            rcount,rsum = dfs(root.right)
            
            tot = root.val + lsum + rsum
            totNode = lcount+rcount+1
            
            if tot//totNode == root.val:
                self.ans += 1
                
            return (totNode,tot)
        
        dfs(root)
        return self.ans
            