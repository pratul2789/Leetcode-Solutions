"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict,deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = dict()
        
        if not node:
            return node
        
        q = deque()
        
        root = Node(node.val,[])
        d[node.val] = root
        q.append(node)
        vis = set()
        vis.add(node.val)
        #print(node.neighbors)
        while q:
            tmp = q.popleft()
            #print(tmp.val)
            root = d[tmp.val]
            #print(len(tmp.neighbors))
            for n in tmp.neighbors:
                if n.val not in d:
                    #print("lol")
                    d[n.val] = Node(n.val,[])
                root.neighbors.append(d[n.val])
                if n.val not in vis:
                    #print("Hola")
                    vis.add(n.val)
                    q.append(n)
                
        return d[node.val]