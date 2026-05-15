class Solution:
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def backtrack(i, curr):
            if len(curr) == len(digits):
                yield curr
                return
            for char in Solution.digitToChar[digits[i]]:
                yield from backtrack(i + 1, curr + char)

        return list(backtrack(0, ""))