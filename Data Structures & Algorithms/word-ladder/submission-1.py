class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        neighbours = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                neighbours[word[:i] + "*" + word[i+1:]].append(word)
        
        def get_neighbours(word):
            for i in range(len(word)):
                for neigh in neighbours[word[:i] + "*" + word[i+1:]]:
                    if neigh == word:
                        continue
                    yield neigh


        front1 = deque([beginWord])
        front2 = deque([endWord])
        visited1 = {beginWord: 1}
        visited2 = {endWord: 1}

        while front1 and front2:
            if len(front1) > len(front2):
                front1, front2 = front2, front1
                visited1, visited2 = visited2, visited1
            
            curr = front1.popleft()
            length = visited1[curr]
            for neigh in get_neighbours(curr):
                if neigh in visited2:
                    return length + visited2[neigh]
                if neigh in visited1:
                    continue
                visited1[neigh] = length + 1
                front1.append(neigh)
        return 0


        