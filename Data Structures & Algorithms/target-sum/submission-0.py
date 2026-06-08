class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {
            0: 1
        }

        for num in nums:
            dp1 = dp
            dp = {}
            for total, count in dp1.items():
                dp[total + num] = dp.get(total + num, 0) + count
                dp[total - num] = dp.get(total +- num, 0) + count
            
        return dp.get(target, 0)


        