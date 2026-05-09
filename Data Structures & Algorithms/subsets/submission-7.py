class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:     
        return [[num for i, num in enumerate(nums) if (mask >> i) & 1] for mask in range(1 << len(nums))]