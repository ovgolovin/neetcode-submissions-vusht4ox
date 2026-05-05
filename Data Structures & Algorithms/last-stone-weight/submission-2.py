import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return self.bucket_sort(stones)


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


    def bucket_sort(self, stones: List[int]) -> int:
        max_weight = max(stones)
        bucket = [0] * (max_weight + 1)
        for stone in stones:
            bucket[stone] += 1
        first = second = max_weight
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            second = min(first - 1, second)
            while second > 0 and bucket[second] == 0:
                second -= 1
            if second == 0:
                return first
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first