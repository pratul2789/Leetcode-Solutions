from collections import defaultdict
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        d = defaultdict(set)
        
        middleGroup = {4,5,6,7}
        leftGroup = {4,5,2,3}
        rightGroup = {8,9,6,7}
        
        for i in reservedSeats:
            if i[1] in middleGroup:
                d[i[0]].add(1)
            
            if i[1] in leftGroup:
                d[i[0]].add(0)
            
            if i[1] in rightGroup:
                d[i[0]].add(2)
                
                
        res = 2*n
        
        for x in d:
            if len(d[x]) == 3:
                res -= 2
            else:
                res -=1 
                
        return res