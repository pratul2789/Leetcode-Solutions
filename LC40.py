class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        vis = set()
        ans = []
        candidates.sort()
        res = set()
        
        def helper(index,path,vis,total,target):
            if tuple(path) in res:
                return 
            
            if total > target:
                return 
            
            if total == target:
                ans.append([i for i in path])
                return
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                helper(i+1,path,vis,total+candidates[i],target)
                path.pop()
        
        helper(0,[],vis,0,target)
        return ans