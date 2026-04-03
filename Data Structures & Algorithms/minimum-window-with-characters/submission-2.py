from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter(t)
        window = Counter()
        need = len(counts)
        have = 0
        best_length = 0

        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == counts[s[right]]:
                have += 1

            while need == have:
                if best_length == 0 or right - left + 1 < best_length:
                    best_length = right - left + 1
                    result = (left, right)
                
                if window[s[left]] == counts[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1

        if best_length == 0:
            return ""
        else:
            return s[result[0]:result[1] + 1]