"""
    A more efficient way of storing the matrixes is to convert them into a common format, maybe string, 
    and then use a visited set.
    
    This problem is similar to 3 puzzle problem or 8 puzzle
"""



from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board:
            return -1
        
        ans = [[1,2,3],[4,5,0]]
        
        if board == ans:
            return 0
        
        q = deque()
        
        sx,sy = -1,-1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    sx,sy = i,j
                    break
        
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        q.append((sx,sy,board,0))
        vis = []
        vis.append(board)
        
        while q:
            x,y,mat,lvl = q.popleft()
            if mat == ans:
                return lvl
            
            for d in dirs:
                r,c = x + d[0], y + d[1]
                tmp = [list(b) for b in mat]
                if r >= 0 and c >= 0 and r < len(board) and c < len(board[0]):
                    swp = tmp[x][y]
                    tmp[x][y] = tmp[r][c] 
                    tmp[r][c] = swp
                    if tmp not in vis:
                        vis.append(tmp)
                        q.append((r,c,tmp,lvl+1))
        return -1