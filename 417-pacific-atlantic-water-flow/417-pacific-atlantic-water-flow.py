class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS,COLS = len(heights), len(heights[0])
        
        pac, atl = set(), set()
        
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def dfs(x,y,prev,vis):
            
            if (x,y) in vis or x < 0 or y < 0 or x >= ROWS or y >= COLS or heights[x][y] < prev:
                return 
            
            vis.add((x,y))
            
            for d in dirs:
                r,c = x + d[0], y + d[1]
                
                dfs(r,c,heights[x][y],vis)
                
                
        for col in range(COLS):
            dfs(0,col,heights[0][col],pac)
            dfs(ROWS - 1,col,heights[ROWS - 1][col],atl)
            
        for row in range(ROWS):
            dfs(row,0,heights[row][0],pac)
            dfs(row,COLS - 1,heights[row][COLS - 1],atl)
            
        res = []
        for i in pac:
            if i in atl:
                res.append([i[0],i[1]])
                
        return res
            
        