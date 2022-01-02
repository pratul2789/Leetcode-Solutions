class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        dp = []
        for i in range(1000):
            dp.append([-1] * 1000)
        def helper(left,index):
            
            if index == len(multipliers):
                return 0
            
            if dp[left][index] != -1:
                return dp[left][index]
            # choose left or choose right
            
            tmp1 = nums[left] * multipliers[index] + helper(left+1,index+1)
            tmp2 = nums[len(nums) - 1 - (index - left)] * multipliers[index] + helper(left,index+1)
            
            dp[left][index] = max(tmp1,tmp2)
            return dp[left][index]
        
        return helper(0,0)
        