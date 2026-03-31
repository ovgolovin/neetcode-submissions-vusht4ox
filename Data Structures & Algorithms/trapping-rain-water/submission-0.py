class Solution:
    def trap(self, height: List[int]) -> int:
        lefts = [0] * len(height)
        left = 0
        for i in range(len(height)):
            lefts[i] = left
            left = max(left, height[i])
        right = 0
        result = 0
        for i in range(len(height) - 1, -1, -1):
            result += max(0, min(lefts[i], right) - height[i])    
            right = max(right, height[i])
        return result