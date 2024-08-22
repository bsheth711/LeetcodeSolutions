class MinStack:

    def __init__(self):
        self.ls = list()
        self.minimum = sys.maxsize
        self.minSet = True
        

    def push(self, val: int) -> None:
        self.ls.append(val) 
        self.minimum = (val < self.minimum) * val + (val >= self.minimum) * self.minimum
        #if val < self.minimum:
            #self.minimum = val

    def pop(self) -> None:
        if self.ls[-1] == self.minimum:
            self.minSet = False 
        del self.ls[-1]

    def top(self) -> int: 
        return self.ls[-1]

    def getMin(self) -> int:
        if not self.minSet:
            self.minimum = min(self.ls)
        
        return self.minimum

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()