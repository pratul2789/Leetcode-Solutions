class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        ans = []
        
        def helper(index,path,total,n,k):

            if total > n or len(path) > k:
                return
            
            if total == n and len(path) == k:
                ans.append([i for i in path])
                return
            
            for i in range(index,10):
                path.append(i)
                helper(i+1,path,total+i,n,k)
                path.pop()
                
        helper(1,[],0,n,k)
        return ans