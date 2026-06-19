class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            elif len(counts) < 2:
                counts[num] = 1
            else:
                for el, count in list(counts.items()):
                    if count == 1:
                        del counts[el]
                    else:
                        counts[el] = count - 1
        
        return [el for el in counts if nums.count(el) > len(nums) // 3]
        