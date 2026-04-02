class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 26
        s1_counts = {}
        s2_counts = {}
        left = 0

        for char in s1:
            s1_count = s1_counts.get(char, 0)
            if s1_count == 0:
                matches -= 1
            s1_counts[char] = s1_count + 1

        for right in range(len(s2)):
            s1_count = s1_counts.get(s2[right], 0)
            s2_count = s2_counts.get(s2[right], 0)
            if s1_count == s2_count + 1:
                matches += 1
            elif s2_count == s1_count:
                matches -= 1
            s2_counts[s2[right]] = s2_count + 1

            if right - left + 1 < len(s1):
                continue

            if right - left + 1 > len(s1):
                s1_count = s1_counts.get(s2[left], 0)
                s2_count = s2_counts[s2[left]]
                if s2_count == s1_count:
                    matches -= 1
                elif s2_count == s1_count + 1:
                    matches += 1
                s2_counts[s2[left]] -= 1
                left += 1

            if matches == 26:
                return True
        return False