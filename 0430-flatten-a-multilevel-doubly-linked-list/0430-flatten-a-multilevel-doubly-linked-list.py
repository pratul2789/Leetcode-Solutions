"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.dum = Node('#')   # a = 3
        self.tail = self.dum   # b = a
        
        def dfs(node):
            if not node:
                return
            
            dumNext = node.next
            dumChild = node.child
            dumPrev = node.prev
            
            # Current Node ki processing
            self.tail.next = node
            #node.prev = None
            node.prev = self.tail
            node.child = None
            #if node.next:
            #    node.next.prev = None
            node.next = None
            #node.
            self.tail = self.tail.next
            
            
            dfs(dumChild)
            dfs(dumNext)
            
        
        dfs(head)
        if self.dum.next:
            self.dum.next.prev = None
        if self.tail:
            self.tail.next = None

        return self.dum.next