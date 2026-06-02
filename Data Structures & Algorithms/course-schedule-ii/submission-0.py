class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        need_counts = [0] * numCourses
        dependents = [set() for _ in range(numCourses)]

        for child, par in prerequisites:
            if child in dependents[par]:
                continue
            dependents[par].add(child)
            need_counts[child] += 1
        
        res = []
        q = deque([course for course, count in enumerate(need_counts) if count == 0])
        
        while q:
            par = q.popleft()
            res.append(par)
            for child in dependents[par]:
                if need_counts[child] == 1:
                    q.append(child)
                else:
                    need_counts[child] -= 1

        if len(res) != numCourses:
            return []

        return res    
        