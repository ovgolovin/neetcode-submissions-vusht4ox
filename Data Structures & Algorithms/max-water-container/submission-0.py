class Solution:
    def maxArea(self, heights: List[int]) -> int:     
        i = 0
        j = len(heights) - 1
        best = 0
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            best = max(area, best)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return best