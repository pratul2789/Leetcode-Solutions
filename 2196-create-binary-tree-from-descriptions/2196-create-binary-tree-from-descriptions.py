# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        
        par = set()
        ch = set()
        d = {}
        adj = {}
        
        for root,child,isLeft in descriptions:
            ch.add(child)
            par.add(root)
            if child not in adj:
                adj[child] = 0
            adj[child] += 1
            
            if child not in d:
                d[child] = TreeNode(child)
                
                
            if root not in d:
                d[root] = TreeNode(root)
                
                
            rootNode = d[root]
            childNode = d[child]
            
            if isLeft == 1:
                rootNode.left = childNode
            else:
                rootNode.right = childNode
                
        
        st = par - ch
        for i in st:
            return d[i]
            
        
        