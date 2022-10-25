class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.toBePrinted = 1
        self.hm = {} #int, string
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        
        self.hm[idKey] = value
        result = []
        
        while self.toBePrinted in self.hm:
            result.append(self.hm[self.toBePrinted])
            self.toBePrinted += 1
        
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)