class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        
        
        arr = [0] * (length+1)
        
        
        for start,end,val in updates:
            arr[start] += val
            arr[end+1] -= val
            
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
            
        return arr[:len(arr)-1]