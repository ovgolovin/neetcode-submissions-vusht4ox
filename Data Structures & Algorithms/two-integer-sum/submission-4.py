class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            complement_idx = seen.get(complement, None)
            if complement_idx is not None:
                return [complement_idx, idx]

            seen[num] = idx