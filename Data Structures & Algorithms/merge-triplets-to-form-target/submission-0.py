class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        total_match = 0
        for triplet in triplets:
            match = 0
            for i, (v, t) in enumerate(zip(triplet, target)):
                if v > t:
                    match = 0
                    break
                if v == t:
                    match |= 1 << i
            total_match |= match
        return total_match == 2 ** len(target) - 1

        