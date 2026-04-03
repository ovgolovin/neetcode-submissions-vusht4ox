class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while True:
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                if result[j] == 0:
                    break
                j += result[j]
        return result