"""
    This was my initial approach, where i was mapping on a bus level.
    This will give you TLE (43/45) passed.

    If you look smartly, you just have to figure out if you can go from 
    Route A to Route B, irrespective of the bus you take.

    It is basically, finding out if you can go from route A to route B.
"""

# from collections import defaultdict,deque
# class Solution(object):
#     def numBusesToDestination(self, routes, source, target):
#         """
#         :type routes: List[List[int]]
#         :type source: int
#         :type target: int
#         :rtype: int
#         """
        
#         if source == target:
#             return 0
        
#         if not routes:
#             return -1
        
        
#         d = defaultdict(list)
#         sb = set()
#         q = deque()
#         vis = set()
#         targets = set()
        
#         for i in range(len(routes)):
#             for k in range(len(routes[i])-1):
#                 for j in range(k+1,len(routes[i])):
#                     if routes[i][k] == source or routes[i][j] == source:
#                         sb.add(i)
#                         q.append((source,i,1))
#                         vis.add((source,i))
#                     if routes[i][k] == target or routes[i][j] == target:
#                         targets.add(i)
#                     d[routes[i][k]].append((routes[i][j],i))
#                     d[routes[i][j]].append((routes[i][k],i))
        
#         if len(d[source]) == 0:
#             return -1
        
#         #print(d)
        
#         while q:
#             sx,pb,lvl = q.popleft()
            
#             for nbrs in d[sx]:
#                 cn,cb = nbrs[0],nbrs[1]
                
#                 if (cn,cb) not in vis:
#                     vis.add((cn,cb))
#                     tlvl = lvl
#                     if cb != pb and cb not in sb:
#                         tlvl += 1
#                     if cn == target or cb in targets:
#                         return tlvl
#                     q.append((cn,cb,tlvl))
#         return -1

from collections import deque,defaultdict

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        
        if not routes:
            return -1
        
        for i in range(len(routes)):
            routes[i] = set(routes[i])
            
        vis = set()
        q = deque()
        des = set()
        d = defaultdict(set)
        
        for i in range(len(routes)):
            
            if source in routes[i]:
                vis.add(i)
                q.append((i,1))
                
            if target in routes[i]:
                des.add(i)
                
            for j in range(i+1,len(routes)):
                if len(routes[i].intersection(routes[j])) > 0:
                    d[i].add(j)
                    d[j].add(i)
                    
        
        while q:
            rt,lvl = q.popleft()
            
            if rt in des:
                return lvl
            
            for nbr in d[rt]:
                if nbr not in vis:
                    vis.add(nbr)
                    q.append((nbr,lvl+1))
            
        return -1