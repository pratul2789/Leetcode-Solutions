class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        
        
        boxes = sorted(boxes,reverse = True)
        
        
        l,r = 0,len(warehouse)-1
        
        count = 0
        i = 0
        while i < len(boxes) and l <= r:
            if boxes[i] <= warehouse[l]:
                l += 1
                count +=1
            elif boxes[i] <= warehouse[r]:
                count += 1
                r -= 1
            i += 1
            
        return count