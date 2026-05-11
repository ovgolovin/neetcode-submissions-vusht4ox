class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        def dfs(i, path, total):
            if total == target:
                yield path.copy()
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break

                path.append(candidates[j])
                yield from dfs(j + 1, path, total + candidates[j])
                path.pop()
        return list(dfs(0, [], 0))   

        