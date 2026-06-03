class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        lowest = (float("+inf"), None)
        tally = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tally += g - c
            lowest = min(lowest, (tally, i))

        return (lowest[1] + 1) % len(gas)
        