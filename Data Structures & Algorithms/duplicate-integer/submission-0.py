class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deduped = set(nums)
        return len(nums) != len(deduped)
        