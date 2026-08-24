from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [start for start, _, _ in jobs]
        n = len(jobs)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            start, end, value = jobs[i]
            next_i = bisect_left(starts, end, i + 1)
            dp[i] = max(dp[i + 1], value + dp[next_i])

        return dp[0]