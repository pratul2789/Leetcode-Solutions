class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return 0
        
        def odd(nums):
            #Change Odd
            ans = 0
            i = 1
            while i < len(nums):
                if i == len(nums) - 1:
                    if nums[i-1] <= nums[i]:
                         ans = ans + (nums[i]-nums[i-1]) + 1
                else:
                    tmp = min(nums[i-1],nums[i+1])
                    if tmp <= nums[i]:
                        ans = ans + (nums[i]-tmp) + 1
                i = i + 2
            return ans
        
        def even(nums):
            ans = 0
            i = 0
            while i < len(nums):
                if i == 0:
                    if nums[i+1] <= nums[i]:
                         ans = ans + (nums[i]-nums[i+1]) + 1
                elif i == len(nums) - 1:
                    if nums[i-1] <= nums[i]:
                         ans = ans + (nums[i]-nums[i-1]) + 1
                else:
                    tmp = min(nums[i-1],nums[i+1])
                    if tmp <= nums[i]:
                        ans = ans + (nums[i]-tmp) + 1
                i = i + 2
            return ans
        
        return min(odd(nums),even(nums))