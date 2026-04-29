class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while i <= j:
            remain = limit - people[j]
            if people[i] <= remain:
                i += 1
            j -= 1
            res += 1
        return res