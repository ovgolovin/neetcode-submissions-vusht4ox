class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)

        for card in hand:
            start = card
            while counts.get(start - 1, 0):
                start -= 1
            while start <= card:
                while counts.get(start, 0):
                    for i in range(start, start + groupSize):
                        if not counts.get(i, 0):
                            return False
                        counts[i] -= 1
                start += 1
        
        return True
        