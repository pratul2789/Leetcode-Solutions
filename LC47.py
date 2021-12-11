class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
        
        vis = set()
        ans = []
        res = set()
        def backtrack(path,nums,vis):
            #print(path)
            if len(path) == len(nums):
                if tuple(path) not in res:
                    res.add(tuple(path))
                    ans.append([i for i in path])
                return 
            for i in range(len(nums)):
                if i not in vis:
                    vis.add(i)
                    path.append(nums[i])
                    backtrack(path,nums,vis)
                    vis.remove(i)
                    path.pop()
                    
            
        backtrack([],nums,vis)
        return ans