class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        
        i,j = 0,0
        
        while i < len(word) and j < len(abbr):
            #print(i,j)
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else : 
                if abbr[j].isdigit():
                    #dig = ""
                    if abbr[j] == "0":
                        return False
                    dig = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        dig = (dig * 10) + int(abbr[j])
                        j += 1
                    #print(dig)
                    if dig >= (len(word) - i + 1):
                        return False
                    i = i + dig
                else:
                    return False
        if i < len(word) or j < len(abbr):
            return False
        return True
            
        