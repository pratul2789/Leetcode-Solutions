"""
    Time Complexity : O(N * 3^L) where N is the number of cells and L is the length of the word, and then 3 directions
    Space Complexity : O(L)
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def backtrack(i,j,board,index,word):
            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            board[i][j] = "#"
            
            res = False
            
            for d in dirs:
                r,c = i + d[0], j + d[1]
                res = res or backtrack(r,c,board,index+1,word)
                if res:
                    return True
                
            board[i][j] = word[index]
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,board,0,word):
                    return True
                
                
        return False