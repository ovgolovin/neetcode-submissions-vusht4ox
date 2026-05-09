import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []    

    def addNum(self, num: int) -> None:
        if self.right and self.right[0] <= num:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left) + 1:
                heapq.heappush(self.left, -heapq.heappop(self.right))
        else:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                heapq.heappush(self.right, -heapq.heappop(self.left))

    
    def findMedian(self) -> float:
        if not self.left and not self.right:
            return None
        elif len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return -self.left[0] + (self.right[0] + self.left[0]) / 2
        