class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for right, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                left = stack.pop()
                result[left] = right - left
            stack.append(right)
        return result