class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits[:]
        for i in range(len(digits) - 1, -1, -1):
            if result[i] < 9:
                result[i] += 1
                return result
            else:
                result[i] = 0
        return [1] + result

        