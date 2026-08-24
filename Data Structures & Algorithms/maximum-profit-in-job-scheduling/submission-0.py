from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        indices = sorted(range(n), key=lambda i: startTime[i])

        dp = [0] * (n + 1)

        search_space = range(n + 1)

        for i in range(n - 1, -1, -1):
            pos = bisect_left(
                search_space,
                endTime[indices[i]],
                lo = i + 1,
                hi = n,
                key = lambda x: startTime[indices[x]]
            )

            dp[i] = max(dp[i + 1], profit[indices[i]] + dp[pos])

        return dp[0]