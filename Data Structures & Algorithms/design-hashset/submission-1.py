class Node:
    def __init__(self, val=None):
        self.val = val
        self.nxt = None    


class MyHashSet:

    def __init__(self):
        self._cap = 10_000
        self._buckets = [Node() for _ in range(self._cap)]
        

    def add(self, key: int) -> None:
        node = self._buckets[key % self._cap]
        while node.nxt:
            if node.nxt.val == key:
                return
            node = node.nxt
        node.nxt = Node(key)
        

    def remove(self, key: int) -> None:
        node = self._buckets[key % self._cap]
        while node.nxt:
            if node.nxt.val == key:
                node.nxt = node.nxt.nxt
                return
            node = node.nxt
        

    def contains(self, key: int) -> bool:
        node = self._buckets[key % self._cap]
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