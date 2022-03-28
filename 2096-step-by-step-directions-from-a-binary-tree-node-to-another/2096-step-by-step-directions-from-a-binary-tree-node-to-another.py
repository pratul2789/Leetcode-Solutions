# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def getLCA(root, startValue, destValue):
            
            if not root:
                return None
            
            if root.val == startValue or root.val == destValue:
                return root
            
            left = getLCA(root.left,startValue,destValue)
            right = getLCA(root.right,startValue,destValue)
            
            if not left:
                return right
            
            if not right:
                return left
            
            return root
        
        
        lcaNode = getLCA(root,startValue,destValue)
        
        if not lcaNode:
            return ""
        
        
        q = deque()
        
        pathToStart = ""
        pathToDest = ""
        
        q.append((lcaNode,""))
        
        while q:
            
            node,pathSoFar = q.popleft()
            
            if node.val == startValue:
                pathToStart = pathSoFar
            
            if node.val == destValue:
                pathToDest = pathSoFar
                
            if node.left:
                q.append((node.left,pathSoFar + "L"))
            
            if node.right:
                q.append((node.right,pathSoFar + "R"))
        
        
        temp = ""
            
        for i in range(len(pathToStart)):
            temp += "U"
                
#         if root.val != startValue and root.val != destValue:
#             # Dono hi Valid hai
#             # Convert startNodePath ko into all U's
            
                
#             return temp + pathToDest
        
#         #One of them is the root. Now we need to make sure that we return all U's if destination is the start node
        
#         if root.val == destValue:
#             temp = ""
            
#             for i in range(len(pathToStart)):
#                 temp += "U"
                
#             return temp
        
        return temp + pathToDest