import itertools

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set(itertools.chain.from_iterable(words))
        descendants = {char: set() for char in chars}
        in_count = {char: 0 for char in chars}

        for word1, word2 in itertools.pairwise(words):
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for char1, char2 in zip(word1, word2):
                if char1 == char2:
                    continue                
                children = descendants[char1]
                if char2 in children:
                    break
                children.add(char2)
                in_count[char2] += 1
                break

        queue = deque([char for char, count in in_count.items() if count == 0])

        res = []

        while queue:
            char = queue.popleft()
            res.append(char)
            for child in descendants[char]:
                if in_count[child] == 1:
                    queue.append(child)
                else:
                    in_count[child] -= 1

        

        if len(res) != len(chars):
            return ""

        return "".join(res)              
        