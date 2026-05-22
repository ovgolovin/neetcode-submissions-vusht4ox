class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = [0] * numCourses
        src_to_dst = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            prereq[dst] += 1
            src_to_dst[src].append(dst)
    
        q = deque()
        for src in range(numCourses):
            if prereq[src] == 0:
                q.append(src)

        taken = 0
        while q:
            src = q.popleft()
            taken += 1
            for dst in src_to_dst[src]:
                if prereq[dst] == 1:
                    q.append(dst)
                else:
                    prereq[dst] -= 1
        
        return taken == numCourses