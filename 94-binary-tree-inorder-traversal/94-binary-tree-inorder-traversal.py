# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while stack or root:
            #print(stack)
            while root:
                #print(root.val)
                stack.append(root)
                root = root.left
            #print("Bleh")
            root = stack.pop()
            res.append(root.val)
            #if root.right:
            root = root.right
                
        return res