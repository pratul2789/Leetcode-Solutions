class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        
        colCoord = ord(coordinates[0]) - ord('a')
        rowCoord = int(coordinates[1])
        
        if colCoord % 2 == 0:
            #if row is odd then black, else white
            if rowCoord % 2 == 1:
                return False
            return True
            
        else:
            #if row is even then black, else white
            if rowCoord % 2 != 1:
                return False
            return True