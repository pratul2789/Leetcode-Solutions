class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            elif s[i] == ')':
                if st:
                    st.pop()
                else:
                    s[i] = ""
        
        for i in st:
            s[i] = ""
        return "".join(s)