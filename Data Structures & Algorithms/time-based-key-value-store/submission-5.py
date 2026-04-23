from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        items = self.store.get(key, [])
        l = 0
        r = len(items)
        while l < r:
            mid = l + (r - l) // 2
            if items[mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1
        index = l - 1
        if index < 0:
            return ""
        return items[index][1]


        
