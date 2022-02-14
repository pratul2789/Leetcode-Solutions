class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        if not grid: 
            return []
        
        if len(grid[0]) == 1:
            return [-1]
        
        
        def canGoNext(i,j):
            if grid[i][j] == 1:
                if j == len(grid[0]) -1:
                    return False
                
                if grid[i][j+1] == -1:
                    return False
                return True
            else:
                if j == 0:
                    return False
                
                if grid[i][j-1] == 1:
                    return False
                return True
            
        
        
        def dfs(row,i,j):
            
            if row == len(grid):
                return j
            
            if canGoNext(i,j):
                if grid[i][j] == 1:
                    return dfs(row+1,i+1,j+1)
                else:
                    return dfs(row+1,i+1,j-1)
            
            return -1
        
        
        res = []
        
        for i in range(len(grid[0])):
            res.append(dfs(0,0,i))
                
        return res