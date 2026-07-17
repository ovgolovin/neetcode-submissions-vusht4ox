from itertools import pairwise
from string import ascii_letters


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        translation = str.maketrans(order, ascii_letters[:len(order)])
        translated = (word.translate(translation) for word in words)
        for word1, word2 in pairwise(translated):
            if word1 > word2:
                return False
        return True


    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        letter_pos = {char: i for i, char in enumerate(order)}
        for word1, word2 in pairwise(words):
            for char1, char2 in zip(word1, word2):
                if char1 == char2:
                    continue
                if letter_pos[char1] > letter_pos[char2]:
                    print(word1, word2)
                    print(char1, char2)
                    print(letter_pos[char1], letter_pos[char2])
                    return False
                break
            else:
                if len(word1) > len(word2):
                    print(word1, word2)
                    return False
        return True



        