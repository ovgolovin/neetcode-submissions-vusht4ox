class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, src, dst in trips:
            events.append((src, num))
            events.append((dst, -num))

        events.sort()

        people = 0
        for point, change in events:
            people += change
            if people > capacity:
                return False
        
        return True
        