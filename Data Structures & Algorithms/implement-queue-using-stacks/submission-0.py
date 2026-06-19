class MyQueue:

    def __init__(self):
        self.inbound = []
        self.outbound = []
        

    def push(self, x: int) -> None:
        self.inbound.append(x)


    def _ensure_outbound(self):
        if not self.outbound:
            while self.inbound:
                self.outbound.append(self.inbound.pop())
        

    def pop(self) -> int:
        self._ensure_outbound()
        return self.outbound.pop()
        

    def peek(self) -> int:
        self._ensure_outbound()
        return self.outbound[-1]
        

    def empty(self) -> bool:
        return not (self.inbound or self.outbound)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()