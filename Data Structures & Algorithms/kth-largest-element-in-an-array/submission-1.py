import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k)

    def heap(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heap[0]

    
    def quick_select(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            nums[right], nums[mid] = nums[mid], nums[right]
            i = left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            if i == len(nums) - k:
                left = i
                break
            elif i < len(nums) - k:
                left = i + 1
            else:
                right = i - 1
        return nums[left] 
        
        