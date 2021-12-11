class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        vis = set()
        ans = []
        def helper(index,path,vis,nums):
            if tuple(path) in vis:
                return
            
            vis.add(tuple(path))
            ans.append([i for i in path])
            
            for i in range(index,len(nums)):
                path.append(nums[i])
                helper(i+1,path,vis,nums)
                path.pop()
                
        
        helper(0,[],vis,nums)
        return ans