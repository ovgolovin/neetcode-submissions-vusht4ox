class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        

    def enQueue(self, value: int) -> bool:
        if self.size >= self.capacity:
            return False
        self.size += 1
        prev = self.dummy
        nxt = self.dummy.next
        node = Node(value, next=nxt, prev=prev)
        prev.next = node
        nxt.prev = node
        return True
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        node = self.dummy.prev
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        return True
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.dummy.prev.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.dummy.next.val        


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()