import heapq
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        d = {}
        
        for i in arr:
            if i not in d:
                d[i] = 0
            d[i] += 1
            
            
        heap = []
        
        for i in d:
            heapq.heappush(heap,(d[i],i))
            
            
        while heap:
            freq,val = heapq.heappop(heap)
            
            if k < freq:
                return len(heap) + 1
            
            k = k - freq
            
        return 0