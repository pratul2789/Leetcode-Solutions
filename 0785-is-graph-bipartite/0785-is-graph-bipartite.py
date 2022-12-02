class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        hm = dict()
        
        hm["B"] = set()
        hm["G"] = set()
        
        def dfs(node, color):
            #print(node,color)
            hm[color].add(node)
            
            set1 = hm["B"]
            set2 = hm["G"]
            
            for nbr in graph[node]:
                if nbr in set1 or nbr in set2:
                    # check conflicting hai kya
                    if nbr in hm[color]:
                        return False
                else:
                    # Safe hai
                    nextColor = "B"
                    if color == "B":
                        nextColor = "G"
                    ans = dfs(nbr,nextColor)
                    if not ans:
                        return False
            return True
        
        for i in range(len(graph)):
            if i in hm["G"] or i in hm["B"]:
                continue
            ans = dfs(i,"G")
            if not ans:
                return False
        #print(hm)        
        return True
            
            