class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed = sorted(changed)
        
        d = {}
        
        for i in changed:
            if i not in d:
                d[i] = 0
            d[i] += 1
            
        
        res = []
        
        for i in changed:
            if len(d) == 0:
                return res
            if i in d:
                pair = 2 * i
                if i == pair and d[i] < 2:
                    return []
                if pair in d:
                    d[pair] -= 1
                    res.append(i)
                    d[i] -= 1
                    if d[i] == 0:
                        del d[i]
                    if pair in d and d[pair] == 0:
                        del d[pair]

        return []