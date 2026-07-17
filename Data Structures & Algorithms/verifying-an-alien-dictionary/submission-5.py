from itertools import pairwise
from string import ascii_lowercase


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        translation = str.maketrans(order, ascii_lowercase)
        translated = (word.translate(translation) for word in words)
        for word1, word2 in pairwise(translated):
            if word1 > word2:
                return False
        return True





        