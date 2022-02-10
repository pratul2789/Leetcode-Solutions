from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        pre = defaultdict(list)
        
        for i in prerequisites:
            pre[i[0]].append(i[1])
            
        res = []
        vis = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            
            if course in vis:
                return True
            
            cycle.add(course)
            
            for node in pre[course]:
                if dfs(node) == False:
                    return False
            
            cycle.remove(course)
            res.append(course)
            vis.add(course)
            return True
        
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return res
        