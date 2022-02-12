class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l = 0
        r = len(s)-1
        flg = True
        rm = ""
        #print("Blah")
        while l <= r:
            #print(l,r)
            if s[l] != s[r]:
                #Case 1, ignore l
                if (s[l:r] == s[l:r][::-1]) or (s[l+1:r+1] == s[l+1:r+1][::-1]):
                    return True
                return False
            l += 1
            r -= 1
        return True
           