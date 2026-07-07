class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if target in visited or "0000" in visited:
            return -1
        if target == "0000":
            return 0

        fronts = [
            { "0000" },
            { target }
        ]
        visited.add("0000")
        visited.add(target)

        steps = 0

        while all(fronts):
            fronts.sort(key=lambda f: len(f))
            
            steps += 1

            new_front = set()
            for node in fronts[0]:
                for i in range(4):
                    for diff in (-1, 1):
                        new_digit = str((int(node[i]) + diff) % 10)
                        nei = node[:i] + new_digit + node[i+1:]
                        if nei in fronts[1]:
                            return steps
                        if nei in visited:
                            continue
                        new_front.add(nei)
                        visited.add(nei)
            fronts[0] = new_front
        
        return -1

        