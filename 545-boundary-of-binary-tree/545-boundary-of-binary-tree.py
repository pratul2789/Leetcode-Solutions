# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        op = []
        if not root:
            return []
            
        def leaves(root,op):
            if root:
                leaves(root.left,op)
                if not root.left and not root.right:
                    op.append(root.val)
                leaves(root.right,op)
                
        def leftB(root,op):
            if root:
                if root.left:
                    op.append(root.val)
                    leftB(root.left,op)
                elif root.right:
                    op.append(root.val)
                    leftB(root.right,op)
                    
        def rightB(root,op):
            if root:
                if root.right:
                    rightB(root.right,op)
                    op.append(root.val)
                elif root.left:
                    rightB(root.left,op)
                    op.append(root.val)
                    
        
        op.append(root.val)
        leftB(root.left,op)
        leaves(root.left,op)
        leaves(root.right,op)
        rightB(root.right,op)
        
        return op