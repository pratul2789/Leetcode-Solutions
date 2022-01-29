class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s or len(s) == 0:
            return True
        
        leftMin, leftMax = 0,0
        
        for br in s:
            
            if br == '(':
                leftMin,leftMax = leftMin + 1, leftMax + 1
                
            if br == ')':
                leftMin,leftMax = leftMin - 1, leftMax - 1
                
            if br == '*':
                leftMin,leftMax = leftMin - 1, leftMax + 1
                
            if leftMax < 0:
                return False
            
            if leftMin < 0:
                leftMin = 0
                
        return leftMin == 0