# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        string = ''
        q = deque()
        q.append((root,str(root.val)))
        res = ''
        while q:
            l1 = len(q)
            for i in range(l1):
                node,val = q.popleft()
                res = res + val + ','
                if node:
                    if node.left:
                        q.append((node.left,str(node.left.val)))
                    else:
                        q.append((None,'X'))

                    if node.right:
                        q.append((node.right,str(node.right.val)))
                    else:
                        q.append((None,'X'))
        #print(res)
        return res
                    
                
        # def helper(root,string):
        #     if root:
        #         string = string + str(root.val) + ","
        #         string = helper(root.left,string)
        #         string = helper(root.right,string)
        #     else:
        #         string = string + 'X,'
        #     return string
        # print(helper(root,string))
        # return helper(root,string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tmp = data.split(',')[:-1]
        print(tmp)
        queue = deque()
        for i in tmp:
            queue.append(i)
        #print(queue)
        if not queue:
            return None
        
        prev = deque()
        rootVal =queue.popleft()
        root = TreeNode(rootVal)
        prev.append(root)
        while prev:
            tmp = len(prev)
            #print(l1,prev)
            for i in range(tmp):
                head = prev.popleft()
                value = queue.popleft()
                if value == 'X':
                    head.left = None
                else:
                    x = TreeNode(value)
                    head.left = x
                    prev.append(x)
                    
                
                value1 = queue.popleft()
                if value1 == 'X':
                    head.right = None
                else:
                    y = TreeNode(value1)
                    head.right = y
                    prev.append(y)
        return root
                
                    
#         def helper(queue):
#             value = queue.popleft()
#             if value == 'X':
#                 return None
#             node = TreeNode(value)
#             node.left = helper(queue)
#             node.right = helper(queue)
            
#             return node
#         return helper(queue)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))