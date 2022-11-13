from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        ans = 0
        if not isConnected:
            return ans
        
        
        vis = set()
        
        n = len(isConnected)
        
        for i in range(n):
            if i not in vis:
                #start bfs
                q = deque()
                q.append(i)
                ans += 1
                while q:
                    node = q.popleft()
                    vis.add(node)
                    for nbr in range(n):
                        if isConnected[node][nbr] == 1 and nbr not in vis:
                            q.append(nbr)
                            
                            
        return ans
                