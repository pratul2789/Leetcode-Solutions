class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if not image:
            return image
        
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def dfs(x,y,color,prevColor):
            
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != prevColor or image[x][y] == color:
                return
            
            image[x][y] = color
            
            for d in dirs:
                r,c = x + d[0], y + d[1]
                dfs(r,c,color,prevColor)
                
        dfs(sr,sc,color,image[sr][sc])
        
        return image