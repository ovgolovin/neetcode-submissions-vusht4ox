from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        needle = Counter(s1)
        window = Counter()
        left = 0

        mismatches = len(needle)

        for right in range(len(s2)):
            if needle[s2[right]] == window[s2[right]] + 1:
                mismatches -= 1
            elif needle[s2[right]] == window[s2[right]]:
                mismatches += 1
            window[s2[right]] += 1

            if right - left + 1 > len(s1):
                if needle[s2[left]] == window[s2[left]]:
                    mismatches += 1
                elif needle[s2[left]] + 1 == window[s2[left]]:
                    mismatches -= 1
                window[s2[left]] -= 1
                left += 1

            if mismatches == 0:
                return True
        return False