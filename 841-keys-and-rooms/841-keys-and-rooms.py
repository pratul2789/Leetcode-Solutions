class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        vis = set()
        
        for i in range(1,len(rooms)):
            vis.add(i)
            
        def dfs(node):
            if len(vis) == 0:
                return
            
            for key in rooms[node]:
                if key in vis:
                    vis.remove(key)
                    dfs(key)
                    
                    
        dfs(0)
        return len(vis) == 0