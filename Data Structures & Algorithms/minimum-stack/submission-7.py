class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val - self.min < 0:
                self.min = val
        

    def pop(self) -> None:
        if not self.stack:
            return
        
        last = self.stack.pop()

        if last < 0:
            self.min = self.min - last


    def top(self) -> int:
        if self.stack[-1] >= 0:
            return self.stack[-1] + self.min
        else:
            return self.min    


    def getMin(self) -> int:
        return self.min       
