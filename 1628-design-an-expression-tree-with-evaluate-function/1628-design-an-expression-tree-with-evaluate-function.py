import abc 
from abc import ABCMeta, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node:
    __metaclass__ = ABCMeta
    # define your fields here
    @abstractmethod
    def evaluate(self):
        pass

class TreeNode(Node):
    
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self):
        return self.val

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: int
        """
        
        stack = []
        
        for i in range(len(postfix)):
            op = postfix[i]
            #if stack:
                #print(stack[-1].val)
            if op.isdigit():
                node = TreeNode(int(op))
                stack.append(node)
            else:
                #print(stack[-1].val)
                right = stack.pop()
                left = stack.pop()
                node = TreeNode()
                if op == "+":
                    node.val = left.val + right.val
                elif op == "-":
                    node.val = left.val - right.val
                elif op == "*":
                    node.val = left.val * right.val
                else:
                    node.val = left.val // right.val
                node.left = left
                node.right = right
                stack.append(node)
        
        return stack.pop()
               

"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        