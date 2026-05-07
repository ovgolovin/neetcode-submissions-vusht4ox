from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_freq_cnt = sum(1 if value == max_freq else 0 for value in counts.values())
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_cnt)