class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        for i in range(len(flowerbed)):
            if n == 0:
                break
                
            if flowerbed[i] == 0:
                if(i == 0 or (i > 0 and flowerbed[i-1] != 1)) and ((i == len(flowerbed) - 1) or i < len(flowerbed) - 1  and flowerbed[i+1] != 1):
                    flowerbed[i] = 1
                    n = n - 1
        #print(flowerbed)
        return n == 0