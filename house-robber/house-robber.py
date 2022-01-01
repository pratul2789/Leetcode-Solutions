class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        
        for i in range(len(nums)+1):
            dp.append([0,0])
            
        #choose, not-choose
        
        for i in range(1,len(dp)):
            dp[i][0] = nums[i-1] + dp[i-1][1]
            dp[i][1] = max(dp[i-1])
        #print(dp)     
        return max(dp[-1])
            