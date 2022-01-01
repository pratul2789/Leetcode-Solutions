class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        arr = [0] * (n+1)
        
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2
        
        for i in range(2,len(arr)):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
            
        return arr[-1]