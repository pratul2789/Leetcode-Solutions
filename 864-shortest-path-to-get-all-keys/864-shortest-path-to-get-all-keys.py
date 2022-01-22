from collections import deque,defaultdict
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
        keySet = [0,0,0,0,0,0,0]
        
        sx,sy = -1,-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    sx,sy = i,j
                else:
                    if grid[i][j] != '#' and grid[i][j] != '.':
                        keySet[ord(grid[i][j].lower()) - ord('a')] = 1
                        
        keySet = tuple(keySet)
        #print(keySet)
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
                        
        vis = set()
        tmp2 = set()
        vis.add((sx,sy,tuple(7 * [0])))
        q = deque()
        q.append((sx,sy,tuple(7 * [0]),0))
        
        
        while q:
            x,y,keys,lvl = q.popleft()
            #print(x,y)
            # if len(keys) == len(keySet):
            #     return lvl+1
            #print(x,y)
            #print(keys)
            for d in dirs:
                r,c = x + d[0], y + d[1]
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] != '#':
                    if (grid[r][c] == '.' or grid[r][c] == '@'):
                        if (r,c,keys) not in vis:
                            vis.add((r,c,keys))
                            q.append((r,c,keys,lvl+1))
                    elif grid[r][c].islower():
                        tmp = list(keys)
                        tmp[ord(grid[r][c]) - ord('a')] = 1
                        if tuple(tmp) == keySet:
                            return lvl+1
                        if (r,c,tuple(tmp)) not in vis:
                            vis.add((r,c,tuple(tmp)))
                            q.append((r,c,tuple(tmp),lvl+1))
                    else:
                        tmp = list(keys)
                        tmp2 = tuple(tmp)
                        if tmp[ord(grid[r][c].lower()) - ord('a')] == 1 and (r,c,tmp2) not in vis:
                            vis.add((r,c,tmp2))
                            q.append((r,c,tmp2,lvl+1))
        return -1
        