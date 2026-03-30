class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        for letter in t:
            letter_count = counts.get(letter, 0) - 1
            if letter_count < 0:
                return False
            counts[letter] = letter_count

        # not need for extra validation because we checked lengths at the top,
        # check for negative counts is sufficient

        return True