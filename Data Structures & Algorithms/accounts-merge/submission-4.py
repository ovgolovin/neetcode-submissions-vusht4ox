from collections import defaultdict, deque
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name

            for email in account[2:]:
                graph[first_email].add(email)
                graph[email].add(first_email)

        visited = set()
        result = []

        for start_email in email_to_name:
            if start_email in visited:
                continue

            component = []
            queue = deque([start_email])
            visited.add(start_email)

            while queue:
                email = queue.popleft()
                component.append(email)

                for neighbor in graph[email]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            result.append([email_to_name[start_email]] + sorted(component))

        return result