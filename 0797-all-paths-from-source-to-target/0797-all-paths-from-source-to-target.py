class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not graph:
            return []
        
        source = 0
        target = len(graph) - 1
        ans = []
        
        def dfs(node,path): 
            path.append(node)
            
            if node == target:
                ans.append([i for i in path])
                return
            
            nbrs = graph[node]
            
            for nbr in nbrs:
                dfs(nbr,path)
                path.pop()
        
            return
        dfs(source,[])
        return ans