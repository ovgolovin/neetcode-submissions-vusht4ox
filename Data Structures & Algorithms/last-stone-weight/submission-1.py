import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return self.heap(stones)


    def heap(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first == second:
                continue
            heapq.heappush(stones, first - second)

        return -stones[0] if stones else 0