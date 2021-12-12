class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        sx,sy = -1,-1
        dx,dy = -1,-1
        validSteps = 0
        
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def helper(i,j,totalSteps,validSteps):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1:
                return 0
            count = 0
            
            if i == dx and j == dy and totalSteps == validSteps:
                return 1
            
            grid[i][j] = -1
            
            for d in dirs:
                r,c = i + d[0], j + d[1]
                
                count += helper(r,c,totalSteps+1,validSteps)
            
            grid[i][j] = 0
            return count
        
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    validSteps += 1
                
                if grid[i][j] == 1:
                    sx,sy = i,j
                    
                if grid[i][j] == 2:
                    dx,dy = i,j
                    
        grid[sx][sy] = 0
        
        return helper(sx,sy,1,validSteps)