from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums) - k + 1)

        queue = deque()
        left = 0
        for right in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)
            if right + 1 < k:
                continue
            left = right - k + 1
            if queue[0] < left:
                queue.popleft()
            result[left] = nums[queue[0]]
        return result