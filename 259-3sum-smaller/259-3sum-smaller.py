class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums) - 1
            while left < right:
                s1 = target - nums[i]
                if nums[left] + nums[right] < s1:
                    ##print(nums[i],nums[left],nums[right])
                    count = count + right - left
                    left = left + 1
                else:
                    right = right - 1
        return(count)
                
            