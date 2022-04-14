# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def helper(s,t):
            if not s and not t:
                return True
            if not t or not s:
                return False
            
            if s.val != t.val:
                return False
            
            if s.val == t.val:
                return helper(s.left,t.left) and helper(s.right,t.right)
            
        
        
        if not t:
            return s
        
        if not s:
            return False
        
        if s.val == t.val:
            if helper(s,t):
                return True
            
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)