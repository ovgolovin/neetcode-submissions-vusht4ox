class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # optimization
            return False 

        def get_counts(a):
            counts = {}
            for letter in a:
                counts[letter] = counts.get(letter, 0) + 1
            return counts
        
        s_counts = get_counts(s)
        t_counts = get_counts(t)

        if len(s_counts) != len(t_counts):
            return False

        for letter, s_count in s_counts.items():
            t_count = t_counts.get(letter, 0)

            if t_count != s_count:
                return False
        
        return True