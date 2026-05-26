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


        def fill(i, curr):
            node = curr.children.get(s[i])
            if node is None:
                return False
            if i == len(s) - 1:
                return node.word_end
            if node.word_end:
                dp[i] = True
                
            return fill(i+1, node)


            





        for i in range(len(s)):
            if i > 0 and not dp[i - 1]:
                continue
            if fill(i, trie.root):
                return True
        
        return False