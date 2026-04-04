from itertools import islice

class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        ordered = sorted(zip(positions, speeds), reverse=True)
        result = 1
        last_time = (target - ordered[0][0]) / ordered[0][1]
        for position, speed in islice(ordered, 1, None):
            time = (target - position) / speed
            if time > last_time:
                result += 1
                last_time = time
        return result