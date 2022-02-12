"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return node
        
        d = dict()
        
        
        def dfs(root):
            
            if root in d:
                return d[root]
            
            node = Node(root.val,[])
            
            d[root] = node
            
            for nbr in root.neighbors:
                tmp = dfs(nbr)
                node.neighbors.append(tmp)
                
            return node
        
        return dfs(node)