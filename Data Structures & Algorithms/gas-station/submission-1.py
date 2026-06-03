class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tally = 0
        for i in range(len(gas)):
            tally += gas[i] - cost[i]
            if tally < 0:
                start = i + 1
                tally = 0

        return start
        