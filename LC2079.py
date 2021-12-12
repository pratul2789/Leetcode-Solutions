class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        if len(tiles) <= 1:
            return len(tiles)
        
        self.ans = 0
        res = set()
        def helper(index,soFar,vis):
            #pritn(soFar)
            if soFar in res:
                return
            
            res.add(soFar)
            
            if len(soFar) >= 1:
                self.ans += 1
                
            for i in range(len(tiles)):
                if i not in vis:
                    vis.add(i)
                    helper(i+1,soFar+tiles[i],vis)
                    vis.remove(i)
        vis = set()
        helper(0,"",vis)
        return self.ans