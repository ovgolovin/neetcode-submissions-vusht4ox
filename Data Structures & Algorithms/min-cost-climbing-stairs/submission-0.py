class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        cur = 0

        for i in range(2, len(cost) + 1):
            cur, prev = min(prev + cost[i-2], cur + cost[i-1]), cur

        return cur
        