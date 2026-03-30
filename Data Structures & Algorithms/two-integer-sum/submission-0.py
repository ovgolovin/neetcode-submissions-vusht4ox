class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements_idx = {target - num: idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            complement_idx = complements_idx.get(num, None)
            if complement_idx is not None and idx != complement_idx:
                return [idx, complement_idx]
        
