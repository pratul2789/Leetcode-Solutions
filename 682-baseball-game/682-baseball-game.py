class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        self.stack = []
        self.total = 0
        def add(num):
            self.total += num
            self.stack.append(num)
            
        def invalidate():
            self.total -= self.stack[-1]
            self.stack.pop()
            
        def double():
            dub = self.stack[-1] * 2
            self.total += dub
            self.stack.append(dub)
            
        def plus():
            tot = self.stack[-1] + self.stack[-2]
            self.total += tot
            self.stack.append(tot)
            
            
        for i in ops:
            if i == "C":
                invalidate()
            elif i == "D":
                double()
            elif i == "+":
                plus()
            else:
                add(int(i))
                
        return self.total