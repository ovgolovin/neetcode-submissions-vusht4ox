class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        result = 0
        left = 0
        max_count = 0
        
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_count = max(max_count, counts[s[right]])

            if right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
