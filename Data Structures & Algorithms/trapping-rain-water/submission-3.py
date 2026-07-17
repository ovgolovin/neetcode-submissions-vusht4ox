class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        result = 0
        while l <= r:
            if left_max < right_max:
                left_max = max(left_max, height[l])
                result += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                result += right_max - height[r]
                r -= 1

        return result