from collections import defaultdict
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        d = defaultdict(list)
        heap = []
        dp = dict()
        
        for i in flights:
            dp[i[0]] = float('inf')
            dp[i[1]] = float('inf')
            d[i[0]].append((i[1],i[2]))
            if i[0] == src:
                heapq.heappush(heap,(0,i[2],i[1]))
                
        
        ans = float('inf')
        
        while heap:
            lvl,bal,node = heapq.heappop(heap)
            
            if node == dst:
                ans = min(ans,bal)
                
            for nbrs in d[node]:
                if lvl + 1 <= k:
                    wt = nbrs[1] + bal
                    if wt < dp[nbrs[0]]:
                        dp[nbrs[0]] = wt
                        heapq.heappush(heap,(lvl+1,nbrs[1]+bal,nbrs[0]))
                                   
                                   
        return ans if ans != float('inf') else -1