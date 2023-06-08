class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapping = {} # keep track of pattern to s mapping 
		# keep track of what s is already being mapped 
		# so you can avoid mapping two different pattern to same thing 
        mapped = set() 
        
        def helper(i, j): 
            if i == len(pattern) and j == len(s): 
                return True 
            if i >= len(pattern) or j >= len(s): # did not work, backtrack
                return 
            if pattern[i] not in mapping: 
                for length in range(1, len(s)-j+1): 
                    if s[j:j+length] not in mapped: # can't map to a mapped string
                        mapped.add(s[j:j+length])
                        mapping[pattern[i]] = s[j:j+length]
                        if helper(i+1, j+length): 
                            return True 
                        mapping.pop(pattern[i])
                        mapped.remove(s[j:j+length])
			# current pattern[i] exists, see if it s[j:] starts with it
            elif s[j:j+len(mapping[pattern[i]])] == mapping[pattern[i]]:  
                if helper(i+1, j+len(mapping[pattern[i]])):
                    #print(mapping)
                    return True
            return False 
        
        x = helper(0, 0)
        print(mapping)
        return x