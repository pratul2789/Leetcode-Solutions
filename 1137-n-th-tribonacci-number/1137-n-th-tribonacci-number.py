from collections import defaultdict
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp =defaultdict(int)
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        def helper(n):
            
            if n in dp:
                return dp[n]
            
            val = helper(n-1) + helper(n-2) + helper(n-3)
            dp[n] = val
            return val
        
        return helper(n)