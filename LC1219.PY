class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        ans = 0
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def helper(i,j):
            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            tmp = grid[i][j]
            grid[i][j] = 0
            lans = tmp
            
            for d in dirs:
                r,c = i + d[0], j + d[1]
                lans = max(lans,tmp + helper(r,c))
                
            grid[i][j] = tmp
            return lans
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ans = max(ans,helper(i,j))
        
                    
        return ans