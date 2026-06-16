class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(0, min(len(s) for s in strs)):
            char = strs[0][i]
            if any(strs[j][i] != char for j in range(1, len(strs))):
                break
            res.append(char)
        return ''.join(res)
        