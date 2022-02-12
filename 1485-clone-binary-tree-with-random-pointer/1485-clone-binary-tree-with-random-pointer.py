# Definition for Node.
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution(object):
    def copyRandomBinaryTree(self, root):
        """
        :type root: Node
        :rtype: NodeCopy
        """
        
        
        d = dict()
        
        def dfs(root):
            if root == None:
                return None
            
            if root in d:
                return d[root]
            
            node = NodeCopy(root.val)
            d[root] = node
            
            node.left = dfs(root.left)
            node.right = dfs(root.right)
            node.random = dfs(root.random)
            
            return node
        
        
            
        return dfs(root)