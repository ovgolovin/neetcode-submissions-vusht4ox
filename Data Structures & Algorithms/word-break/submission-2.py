class Node:
    def __init__(self):
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root
        for char in word:
            node = curr.children.get(char)
            if node is None:
                node = Node()
                curr.children[char] = node
            curr = node
        curr.word_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        trie = Trie()
        for word in wordDict:
            trie.add(word)


        for i in range(len(s)):
            if i > 0 and not dp[i - 1]:
                continue
            node = trie.root
            for j in range(i, len(s)):
                node = node.children.get(s[j])
                if node is None:
                    break
                if node.word_end:
                    dp[j] = True
            if node and node.word_end:
                return True
        
        return False