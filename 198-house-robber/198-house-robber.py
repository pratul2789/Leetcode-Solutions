from collections import defaultdict
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = defaultdict(int)
        def helper(ch,n):
            #print(ch)
            if ch >= n:
                return 0
            if ch in dp:
                return dp[ch]
            val = max(helper(ch+2,n) + nums[ch], helper(ch+1,n))
            dp[ch] = val
            return val
        
        return helper(0,len(nums))