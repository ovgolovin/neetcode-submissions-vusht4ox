class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 1

    def connect(self, other):
        self.next = other
        other.prev = self


class DoubleLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.dummy.connect(self.dummy)
        self.size = 0

    def __len__(self):
        return self.size
    
    def pop(self, node):
        node.prev.connect(node.next)
        self.size -= 1
        return node

    def pop_left(self):
        if self.size == 0:
            return None

        return self.pop(self.dummy.prev)

    def append(self, node):
        last = self.dummy.next
        self.dummy.connect(node)
        node.connect(last)
        self.size += 1



class LFUCache:

    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError(f"Invalid capacity {capacity}. Should be > 0")
        self.capacity = capacity
        self.size = 0
        self.key_to_node = {}
        self.freq_to_nodes = defaultdict(DoubleLinkedList)
        self.min_freq = 1


    def _increment_usage(self, node):
        old_freq = node.freq
        new_freq = old_freq + 1
        freq_nodes = self.freq_to_nodes[old_freq]
        freq_nodes.pop(node)
        node.freq = new_freq
        if old_freq == self.min_freq and len(freq_nodes) == 0:
            self.min_freq = new_freq

        self.freq_to_nodes[new_freq].append(node)
      

    def get(self, key: int) -> int:
        node = self.key_to_node.get(key)
        if node is None:
            return -1

        self._increment_usage(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        node = self.key_to_node.get(key)
        
        # key exists
        if node is not None:
            self._increment_usage(node)
            node.val = value
            return

        # need to add new key
        if self.size == self.capacity:
            evict_node = self.freq_to_nodes[self.min_freq].pop_left()
            del self.key_to_node[evict_node.key]
            self.size -= 1

        node = Node(key, value)
        self.key_to_node[key] = node
        self.freq_to_nodes[1].append(node)
        self.min_freq = 1
        self.size += 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)