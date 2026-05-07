

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k)

    def heap(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heap[0]

    
    def quick_select(self, nums: List[int], k: int) -> int:
        import random
        target = len(nums) - k
        left = 0
        right = len(nums) - 1
        while left < right:
            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]
            i = left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            if i == target:
                return nums[i]
            elif i < target:
                left = i + 1
            else:
                right = i - 1
        return nums[left] 
        
        