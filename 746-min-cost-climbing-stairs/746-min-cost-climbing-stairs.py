from collections import defaultdict
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        dp = defaultdict(int)
        def helper(cs, n):
            if cs == n:
                return 0
            
            if cs > n:
                return float('inf')
            
            if dp[cs] != 0:
                return dp[cs]
            
            cc = cost[cs] + min(helper(cs+1, n) ,helper(cs + 2, n))
            
            dp[cs] = cc
            
            return cc
        
        return min(helper(0,len(cost)), helper(1,len(cost)))