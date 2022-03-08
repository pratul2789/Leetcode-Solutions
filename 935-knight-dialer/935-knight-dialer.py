#from functools import lru_cache
from collections import defaultdict
class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        mat = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        
        dirs = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
        
        dp = defaultdict(int)
        
        def backtrack(i,j,k):
            if k == 0:
                return 1
            
            if k == 0:
                return 0
            
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            
            
            count = 0
            
            for d in dirs:
                r,c = i + d[0],j + d[1]
                if r >= 0 and c >= 0 and r < 4 and c < 3:
                    if (r == 3 and c == 0) or (r == 3 and c == 2):
                        continue
                    count += backtrack(r,c,k-1)
                
            #mat[i][j] = tmp
            dp[(i,j,k)] += count
            return count
            
        ans = 0
        
        for i in range(4):
            for j in range(3):
                if (i == 3 and j == 0) or (i == 3 and j == 2):
                    continue
                ans += backtrack(i,j,n-1)
        
        #ans += backtrack(0,0,n-1,[])
                
        return ans % ((10 **9) + 7)