class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        ans = []
        def helper(path,nums,vis):
            
            if len(path) == len(nums):
                ans.append([i for i in path])
                return
                
            for i in range(len(nums)):
                if i not in vis:
                    vis.add(i)
                    path.append(nums[i])
                    helper(path,nums,vis)
                    vis.remove(i)
                    path.pop()
        
        vis = set()
        helper([],nums,vis)
        return ans