class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        
        
        def mergeSort(nums):
            if len(nums) > 1:
                
                mid = len(nums) // 2
                
                l = nums[:mid]
                
                r = nums[mid:]
                
                mergeSort(l)
                
                mergeSort(r)
                
                i = 0
                j = 0
                k = 0
                
                while i < len(l) and j < len(r):
                    n1 = l[i]
                    n2 = r[j]
                    
                    n11 = str(n1) + str(n2)
                    n21 = str(n2) + str(n1)
                    
                    if n11 > n21:
                        nums[k] = l[i]
                        i += 1
                    else:
                        nums[k] = r[j]
                        j += 1
                        
                    k += 1
                    
                while i < len(l):
                    nums[k] = l[i]
                    i += 1
                    k += 1
                    
                while j < len(r):
                    nums[k] = r[j]
                    j += 1
                    k += 1
                    
        mergeSort(nums)
        res = ""
        if nums[0] == 0:
            return "0"
        for i in range(len(nums)):
            res += str(nums[i])
        
        return res
        #return "".join(nums)
                    