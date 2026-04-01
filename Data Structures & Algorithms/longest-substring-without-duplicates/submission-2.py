class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in last_pos and last_pos[s[r]] >= l:
                l = last_pos[s[r]] + 1            
            last_pos[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest