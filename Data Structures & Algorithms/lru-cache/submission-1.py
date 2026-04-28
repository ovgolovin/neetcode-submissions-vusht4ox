
class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.dummy = Node()
        self.dummy.next = self.dummy.prev = self.dummy

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def get_oldest(self):
        return self.dummy.prev


    def add(self, node):
        nxt = self.dummy.next
        self.dummy.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = self.dummy


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kmap = {}
        self.nodes = LinkedList()
        
    def get(self, key: int) -> int:
        node = self.kmap.get(key)
        if node is None:
            return -1
        else:
            self.nodes.remove(node)
            self.nodes.add(node)
            return node.val
        
    def put(self, key: int, value: int) -> None:
        node = self.kmap.get(key)
        if node is not None:
            self.nodes.remove(node)
            self.nodes.add(node)
            node.val = value
        else:
            if len(self.kmap) >= self.capacity:
                oldest = self.nodes.get_oldest()
                self.nodes.remove(oldest)
                del self.kmap[oldest.key]
            node = Node(key, value)
            self.kmap[key] = node
            self.nodes.add(node)





