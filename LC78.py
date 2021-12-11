class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def helper(index,nums,path):
            ans.append([i for i in path])    
            
            if len(path) == len(nums):
                return
            
            for i in range(index,len(nums)):
                path.append(nums[i])
                helper(i+1,nums,path)
                path.pop()
                
        
        helper(0,nums,[])
        return ans