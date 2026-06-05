class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dst in tickets:
            adj.setdefault(src, []).append(dst)

        for src, dsts in adj.items():
            dsts.sort(reverse=True)

        stack = ['JFK']
        res = []

        while stack:
            neighbours = adj.get(stack[-1])
            if not neighbours:
                res.append(stack.pop())
            else:
                stack.append(neighbours.pop())

        return res[::-1]
        