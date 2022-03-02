from collections import defaultdict
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        arr = sorted(arr)
        
        d = dict()
        for i in arr:
            if i not in d:
                d[i] = 0
            d[i] += 1
            
            
        for i in arr:
            if len(d) == 0:
                return True
            if i in d:
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
            
                if i < 0:
                    if (i) % 2 != 0:
                        return False
                    comp = i // 2
                else:
                    comp = i * 2

                if comp not in d:
                    return False

                d[comp] -= 1
                if d[comp] == 0:
                    del d[comp]
            
        return False
        