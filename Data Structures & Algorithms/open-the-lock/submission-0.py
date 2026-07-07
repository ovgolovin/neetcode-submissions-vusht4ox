class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if target in visited or "0000" in visited:
            return -1
        if target == "0000":
            return 0

        front_small = { "0000" }
        front_large = { target }
        visited.add("0000")
        visited.add(target)

        steps = 0

        while front_small and front_large:
            if len(front_small) > len(front_large):
                front_small, front_large = front_large, front_small
            
            steps += 1

            new_front = set()
            for node in front_small:
                for i in range(4):
                    for diff in (-1, 1):
                        new_digit = str((int(node[i]) + diff) % 10)
                        nei = node[:i] + new_digit + node[i+1:]
                        if nei in front_large:
                            return steps
                        if nei in visited:
                            continue
                        new_front.add(nei)
                        visited.add(nei)
            front_small = new_front
        
        return -1

        