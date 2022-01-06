class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        
        res = [False] * len(heights)
        
        mx = heights[-1]
        
        res[-1] = True
        
        for i in range(len(heights)-2,-1,-1):
            if heights[i] > mx:
                mx = heights[i]
                res[i] = True
        ret = []
        
        for i in range(len(res)):
            if res[i]:
                ret.append(i)
                
        return ret
        
        