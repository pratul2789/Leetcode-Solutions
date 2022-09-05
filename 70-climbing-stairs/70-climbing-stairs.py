from collections import defaultdict
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = defaultdict(int)
        def helper(cs, n):
            if cs > n:
                return 0
            if dp[cs] != 0:
                return dp[cs]
            
            if cs == n:
                return 1
            
            ways = helper(cs+1, n) + helper(cs+2, n)
            dp[cs] = ways
            return dp[cs]
        
        return helper(0, n)