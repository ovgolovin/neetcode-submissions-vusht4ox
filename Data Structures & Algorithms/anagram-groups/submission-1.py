from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def char_count(s):
            digest = [0] * (ord('z') - ord('a') + 1)
            for letter in s:
                digest[ord(letter) - ord('a')] += 1
            return tuple(digest)
        
        groups = defaultdict(list)
        for s in strs:
            groups[char_count(s)].append(s)
        return list(groups.values())