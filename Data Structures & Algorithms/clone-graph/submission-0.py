"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {
            node: Node(node.val)
        }

        queue = deque([node])

        while queue:
            curr = queue.popleft()
            curr_new = old_to_new[curr]
            for neighbor in curr.neighbors:
                neighbor_new = old_to_new.get(neighbor)
                if neighbor_new is None:
                    neighbor_new = Node(neighbor.val)
                    old_to_new[neighbor] = neighbor_new
                    queue.append(neighbor)
                curr_new.neighbors.append(neighbor_new)

        return old_to_new[node]
                    


        