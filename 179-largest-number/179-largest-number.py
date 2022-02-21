class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        def comp(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(comp))
        if int(nums[0]) == 0:
            return "0"
        return "".join(nums)