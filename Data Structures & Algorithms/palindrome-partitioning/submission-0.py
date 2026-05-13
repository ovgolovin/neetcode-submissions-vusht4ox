class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if (s[i] == s[j]
                    and (l <= 2
                        or dp[i + 1][j - 1])):
                    dp[i][j] = True

        def dfs(i, parts):
            if i == n:
                yield parts.copy()
                return
            
            for j in range(i, n):
                if dp[i][j]:
                    parts.append(s[i:j+1])
                    yield from dfs(j + 1, parts)
                    parts.pop()

        return list(dfs(0, []))
                    
