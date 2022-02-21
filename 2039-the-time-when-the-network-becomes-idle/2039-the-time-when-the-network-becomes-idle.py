from collections import defaultdict,deque
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        adj = defaultdict(list)
        shortestPath = defaultdict(int)
        
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def bfs():
            q = deque()
            vis = set()
            vis.add(0)
            q.append(0)
            level = 0
            while q:
                l1 = len(q)
                
                for _ in range(l1):
                    node = q.popleft()
                    
                    shortestPath[node] = level
                    
                    for nbr in adj[node]:
                        if nbr not in vis:
                            vis.add(nbr)
                            q.append(nbr)         
                level += 1
        
        bfs()
        ans = 0
        for node in range(1,len(patience)):
            pat = patience[node]
            
            fullPath = (shortestPath[node] * 2)
            
            extraPackets = (fullPath - 1) // pat
            
            lastPacketSent = extraPackets * pat
            
            ans = max(ans,lastPacketSent + fullPath)
            
        return ans + 1