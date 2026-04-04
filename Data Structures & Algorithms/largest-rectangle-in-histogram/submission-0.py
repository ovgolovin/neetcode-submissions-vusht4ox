class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights) + 1):
            while stack:
                if i == len(heights) or heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                elif heights[i] == heights[stack[-1]]:
                    stack.pop()
                else:
                    break
            stack.append(i)
        return max_area
        