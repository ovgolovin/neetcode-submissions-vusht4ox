class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Stack holds (index, current_subset)
        stack = [(0, [])]
        
        while stack:
            i, subset = stack.pop()
            
            if i >= len(nums):
                res.append(subset)
                continue
            
            # Branch 1: skip nums[i]
            stack.append((i + 1, subset))
            
            # Branch 2: include nums[i]
            stack.append((i + 1, subset + [nums[i]]))
        
        return res