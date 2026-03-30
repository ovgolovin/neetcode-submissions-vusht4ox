class Solution:

    def encode(self, strs: List[str]) -> str:
        def stream(strs):
            for s in strs:
                for c in s:
                    if c == "#":
                        yield "##"
                    else:
                        yield c
                yield "#0"
        return ''.join(stream(strs))

    def decode(self, s: str) -> List[str]:
        def parse(s):
            i = 0
            def consume_before_sep():
                nonlocal i
                while i < len(s):
                    if s[i] == "#":
                        if i == len(s) - 1:
                            raise ValueError(f"Invalid escape char at {i}")
                        if s[i + 1] == "0":
                            i += 2
                            return
                        elif s[i + 1] == "#":
                            yield "#"
                            i += 2
                        else:
                            raise ValueError("Invalid escape char")
                    else:
                        yield s[i]
                        i += 1

            while i < len(s):
                yield ''.join(consume_before_sep())
                

        return list(parse(s))