from collections import deque
class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        q = deque()
        x,y = -1,-1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    x = i
                    y = j
                    break
        if x == -1 and y == -1:
            return -1
        
        q.append((x,y))
        ans = 0
        grid[x][y] = 'X'

        #print(x,y)
        while q:
            l = len(q)
            for _ in range(l):
                x,y = q.popleft()
                #print(x,y,path)
                ##if grid[x][y] == '#':
                ##    return ans

                for d in dirs:
                    r,c = x + d[0], y + d[1]
                    if r >=0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 'X':
                        #path.append((r,c))
                        if grid[r][c] == '#':
                            return ans + 1
                        grid[r][c] = 'X'
                        q.append((r,c))
                        
            ans = ans + 1
                        #path.pop()
        
        return -1
                