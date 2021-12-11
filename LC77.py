class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        if n == 0:
            return []
        ans = []
        def helper(index,path,k,n):
            
            if len(path) == k:
                ans.append([i for i in path])
                
            for i in range(index,n+1):
                path.append(i)
                helper(i+1,path,k,n)
                path.pop()
                
        helper(1,[],k,n)
        return ans