class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i = 0
        j = len(people) - 1
        count = 0
        while i < j:
            count += 1
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1

        if i == j:
            count += 1

        return count
        