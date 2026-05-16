from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Node:
    children: defaultdict = field(default_factory=lambda: defaultdict(Node))
    word_end: bool = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.word_end = True
        

    def search(self, word: str) -> bool:
        return self._search_dfs(word, 0, self.root)


    def _search_dfs(self, word, i, curr):
        if i == len(word):
            return curr.word_end
        if word[i] == '.':
            return any((self._search_dfs(word, i + 1, node) for node in curr.children.values()))

        node = curr.children.get(word[i])
        return self._search_dfs(word, i + 1, node) if node else False