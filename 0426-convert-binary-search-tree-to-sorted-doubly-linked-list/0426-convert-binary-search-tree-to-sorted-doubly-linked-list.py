"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return root
        
        
        self.head = None
        self.curr = self.head
        
        def dfs(root, par):
            if not root:
                return None
           # print ("======= " + str(root.val))
            left = dfs(root.left, None)
            
            if not self.head:
                #print("heahaadad")
                self.head = root
                self.curr = self.head
            else:
                self.curr.right = root
                root.left = self.curr
                
                
            self.curr = root
            
            right = dfs(root.right, root)
            return root
        
        dfs(root,None)
        self.head.left = self.curr
        self.curr.right = self.head
        return self.head