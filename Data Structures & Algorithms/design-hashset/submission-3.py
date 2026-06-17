class Node:
    def __init__(self, val=None):
        self.val = val
        self.nxt = None    


class MyHashSet:

    def __init__(self):
        self._size = 20
        self._count = 0
        self._buckets = [Node() for _ in range(self._size)]


    def __iter__(self):     
        for node in self._buckets:
            while node.nxt:
                yield node.nxt.val
                node = node.nxt
            

    def _increase_capacity(self):
        new_size = self._size * 2
        new_buckets = [Node() for _ in range(new_size)]
        for val in self:
            node = new_buckets[val % new_size]
            while node.nxt:
                node = node.nxt
            node.nxt = Node(val)
        self._size = new_size
        self._buckets = new_buckets                


        
    def add(self, key: int) -> None:
        node = self._buckets[key % self._size]
        while node.nxt:
            if node.nxt.val == key:
                return
            node = node.nxt
        node.nxt = Node(key)
        self._count += 1
        if self._count > self._size * 0.8:
            self._increase_capacity()
        

    def remove(self, key: int) -> None:
        node = self._buckets[key % self._size]
        while node.nxt:
            if node.nxt.val == key:
                node.nxt = node.nxt.nxt
                self._count -= 1
                return
            node = node.nxt


    def contains(self, key: int) -> bool:
        node = self._buckets[key % self._size]
        while node.nxt:
            if node.nxt.val == key:
                return True
            node = node.nxt
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)