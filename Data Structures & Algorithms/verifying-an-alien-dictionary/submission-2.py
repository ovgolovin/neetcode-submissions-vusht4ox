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





        