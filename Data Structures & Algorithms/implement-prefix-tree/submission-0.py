from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word_end = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.word_end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            cur = cur.children.get(char)
            if not cur:
                return False
        return cur.word_end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            cur = cur.children.get(char)
            if not cur:
                return False
        return True       
        