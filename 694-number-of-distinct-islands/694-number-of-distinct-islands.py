from collections import deque
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        vis = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q = deque()
                    q.append((i,j))
                    grid[i][j] = 0
                    islands = [(i-i,j-j)]
                    while q:
                        x,y = q.popleft()
                        for d in dirs:
                            r,c = x + d[0],y + d[1]
                            if r >= 0 and r < len(grid) and c >=0 and c < len(grid[0]) and grid[r][c] == 1:
                                islands.append((r-i,c-j))
                                grid[r][c] = 0
                                q.append((r,c))
                    vis.add(tuple(islands))
        #print(vis)
        return len(vis)