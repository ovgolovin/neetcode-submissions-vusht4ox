class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        nums.sort()

        def k_sum(k, prefix, start, target):
            if k > 2:
                for i in range(start, n - k + 1):
                    if sum(nums[x] for x in range(i, i + k)) > target:
                        break
                    if nums[i] + sum(nums[x] for x in range(n - k + 1, n)) < target:
                        continue
                    if i > start and nums[i - 1] == nums[i]:
                        continue
                    prefix.append(nums[i])
                    yield from k_sum(k - 1, prefix, i + 1, target - nums[i])
                    prefix.pop()
            elif k == 2:
                i = start
                j = n - 1
                while i < j:
                    curr = nums[i] + nums[j]
                    if curr == target:
                        yield prefix + [nums[i], nums[j]]
                    if curr <= target:
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                        i += 1
                    if curr >= target:
                        while i < j and nums[j - 1] == nums[j]:
                            j -= 1
                        j -= 1                         
            else:
                return


        return list(k_sum(4, [], 0, target))

        