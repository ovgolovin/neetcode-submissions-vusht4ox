class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        def helper(s):
            i = 0
            while i < len(s):
                j = s.index('#', i)
                length = int(s[i:j])
                yield s[j+1:j+1+length]
                i = j + 1 + length

        return list(helper(s))