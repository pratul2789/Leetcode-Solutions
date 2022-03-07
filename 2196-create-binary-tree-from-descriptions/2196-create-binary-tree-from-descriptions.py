# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        par = set()
        ch = set()
        d = {}
        adj = {}
        
        for root,child,isLeft in descriptions:
            ch.add(child)
            par.add(root)
            
            
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
                
        #print(par) 
        st = par - ch
        for i in st:
            return d[i]