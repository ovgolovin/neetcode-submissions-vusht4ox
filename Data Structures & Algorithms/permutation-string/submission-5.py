from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        have = Counter()
        left = 0

        mismatches = len(need)

        for right in range(len(s2)):
            if need[s2[right]] == have[s2[right]] + 1:
                mismatches -= 1
            elif need[s2[right]] == have[s2[right]]:
                mismatches += 1
            have[s2[right]] += 1

            if right - left + 1 > len(s1):
                if need[s2[left]] == have[s2[left]]:
                    mismatches += 1
                elif need[s2[left]] + 1 == have[s2[left]]:
                    mismatches -= 1
                have[s2[left]] -= 1
                left += 1

            if mismatches == 0:
                return True
        return False