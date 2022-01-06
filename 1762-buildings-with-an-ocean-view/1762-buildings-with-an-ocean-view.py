class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        res = []
        res.append(len(heights)-1)
        mx = heights[-1]
        for i in range(len(heights)-2,-1,-1):
            if heights[i] > mx:
                mx = heights[i]
                res.append(i)
                
        return res[::-1]
        