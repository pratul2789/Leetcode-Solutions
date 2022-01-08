class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        
        colCoord = ord(coordinates[0]) - ord('a') + 1
        rowCoord = int(coordinates[1])
        
        return not ((colCoord%2 == 0 and rowCoord%2 == 0) or (colCoord%2 != 0 and rowCoord%2 != 0))