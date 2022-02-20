import heapq
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        adj = defaultdict(list)
        
        for s,d,w in times:
            adj[s].append((d,w))
            
        heap = []
        
        vis = set()
        
        heapq.heappush(heap,(0,k))
        #vis.add(k)
        ans = 0
        
        while heap:
            wt,node = heapq.heappop(heap)
            if node not in vis:
            #vis.add(node)
                vis.add(node)
                ans = max(ans,wt)
                for nbr,wt2 in adj[node]:
                    if nbr not in vis:
                        #vis.add(nbr)
                        heapq.heappush(heap,(wt + wt2,nbr))
                    
        
        if len(vis) == n:
            return ans
        
        return -1