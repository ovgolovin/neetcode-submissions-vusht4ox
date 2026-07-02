class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * n
        trusts_somebody = [False] * n
        for src, dst in trust:
            trusts_somebody[src - 1] = True
            trusted_count[dst - 1] += 1

        for i in range(n):
            if (not trusts_somebody[i]) and trusted_count[i] == n - 1:
                return i + 1

        return -1
        