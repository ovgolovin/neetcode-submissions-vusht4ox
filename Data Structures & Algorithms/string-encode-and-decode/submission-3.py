class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{chr(len(s))}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        def helper(s):
            i = 0
            while i < len(s):
                length = ord(s[i])
                i += 1
                yield s[i:i+length]
                i += length

        return list(helper(s))