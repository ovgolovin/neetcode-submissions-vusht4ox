from itertools import chain

class TrieNode:
    def __init__(self, char, parent = None):
        self.children = {}
        self.word_idx = None
        self.parent = parent
        self.refs = 0
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def add(self, word, idx):
        curr = self.root
        curr.refs += 1
        for char in word:
            node = curr.children.get(char)
            if not node:
                node = TrieNode(char, parent = curr)
                curr.children[char] = node
            curr = node
            curr.refs += 1
        curr.word_idx = idx

    def unref(self, node):
        if node.word_idx is None:
            return
        node.word_idx = None
        while node:
            node.refs -= 1
            parent = node.parent
            if node.refs == 0 and parent is not None:
                del parent.children[node.char]
            node = parent


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for idx, word in enumerate(words):
            trie.add(word, idx)   

        n = len(board)
        m = len(board[0])

        visited = object()

        def dfs(i, j, parent):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] is visited:
                return
            char = board[i][j]
            node = parent.children.get(char)
            if node is None:
                return
            if node.word_idx is not None:
                yield words[node.word_idx]
                trie.unref(node)
            if node.refs == 0:
                return
            board[i][j] = visited
            for neighbour in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                yield from dfs(neighbour[0], neighbour[1], node)
            board[i][j] = char

        return list(chain.from_iterable((dfs(i, j, trie.root) for i in range(n) for j in range(m))))
            


            