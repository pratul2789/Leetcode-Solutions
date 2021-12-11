class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if target == 0:
            return []
        
        ans = []
        
        def backtrack(path,index,total,target):

            if total > target:
                return
            
            if total == target:
                ans.append([i for i in path])
                return
            
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(path,i,total+candidates[i],target)
                path.pop()
                
        backtrack([],0,0,target)
        return ans