class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        adj = defaultdict(set)
        for row in accounts:
            name = row[0]
            for i in range(1, len(row)):
                email_to_name[row[i]] = name
            for i in range(2, len(row)):
                adj[row[1]].add(row[i])
                adj[row[i]].add(row[1])

        visited = set()

        def bfs(start_email):
            group = []
            queue = deque([start_email])
            visited.add(start_email)
            while queue:
                email = queue.popleft()
                group.append(email)
                for nei in adj[email]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append(nei)
            return group

        result = []

        for email in email_to_name:
            if email in visited:
                continue
            group = bfs(email)
            result.append([email_to_name[email]] + sorted(group))

        return result

