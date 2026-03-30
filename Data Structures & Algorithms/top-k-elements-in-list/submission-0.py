from itertools import islice, chain

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freqs = [[] for _ in range(len(nums))]

        for num, count in counts.items():
            freqs[len(freqs) - count].append(num)

        return list(islice(chain.from_iterable(freqs), k))