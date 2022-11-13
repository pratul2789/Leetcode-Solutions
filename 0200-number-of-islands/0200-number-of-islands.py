class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ans = 0
        
        if not grid:
            return 0
        
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return 
            
            grid[i][j] = "0"
            for d in dirs:
                r,c = i + d[0],j + d[1]
                dfs(r,c)
                
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)
                    
                    
        return ans
            