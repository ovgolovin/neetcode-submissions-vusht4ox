from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        items = self.store.get(key, [])
        index = bisect_right(items, timestamp, key=lambda x: x[0]) - 1
        if index < 0:
            return ""
        return items[index][1]


        
