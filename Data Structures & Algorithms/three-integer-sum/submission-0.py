class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        found = set()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    if (nums[j], nums[k]) not in found:
                        found.add((nums[j], nums[k]))
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif cur > 0:
                    k -= 1
                else:
                    j += 1


        return result
        