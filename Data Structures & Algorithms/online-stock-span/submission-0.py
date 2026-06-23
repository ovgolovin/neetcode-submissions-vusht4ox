class StockSpanner:

    def __init__(self):
        self.idx = 0
        self.stack = [(0, float("inf"))]
        

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack[-1][1] <= price:
            self.stack.pop()
        span = self.idx - self.stack[-1][0]
        self.stack.append((self.idx, price))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)