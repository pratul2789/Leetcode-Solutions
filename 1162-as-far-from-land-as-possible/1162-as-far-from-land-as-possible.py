from collections import deque
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return -1
        
        
        q = deque()
        flg = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    flg = True
                if grid[i][j] == 1:
                    q.append((i,j,0))
                
        if not flg or len(q) == 0:
            return -1
        
        ans = 0
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]

        while q:
            x,y,lvl = q.popleft()
            
            ans = max(ans,lvl)
            
            for d in dirs:
                r,c = x + d[0], y + d[1]
                
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == 0:
                    grid[r][c] = 1
                    q.append((r,c,lvl+1))
        
        return ans
                    