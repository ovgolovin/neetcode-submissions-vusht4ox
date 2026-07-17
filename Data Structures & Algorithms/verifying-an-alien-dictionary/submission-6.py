from itertools import pairwise, zip_longest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}
        end = object()

        for first, second in pairwise(words):
            for a, b in zip_longest(first, second, fillvalue=end):
                if a == b:
                    continue

                # second ended first: "apple" before "app"
                if b is end:
                    return False

                # first ended first, or differing characters are ordered
                if a is end or rank[a] < rank[b]:
                    break

                return False

        return True