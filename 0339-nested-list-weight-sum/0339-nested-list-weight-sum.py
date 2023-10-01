# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        if not nestedList:
            return 0
        
        """
        def dfs(arr, depth):
            total = 0
            
            for i in arr:
                if i.isInteger():
                    total += i.getInteger() * depth
                else:
                    total += dfs(i.getList(), depth + 1)
                    
            return total
        return dfs(nestedList, 1)"""
        
        q = deque([])
        for i in nestedList:
            q.append(i)
        
        dep = 1
        tot = 0
        while q:
            l = len(q)
            for _ in range(l):
                ele = q.popleft()
                if ele.isInteger():
                    tot = tot + (dep * ele.getInteger())
                else:
                    for j in ele.getList():
                        q.append(j)
            dep += 1
        return tot
        
        
            
        