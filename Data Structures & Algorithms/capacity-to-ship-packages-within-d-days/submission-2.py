class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l + r) // 2
            tot = 1
            rem = m
            for i in range(len(weights)):
                if weights[i] <= rem:
                    rem -= weights[i]
                else:
                    tot += 1
                    rem = m - weights[i]
            if tot <= days:
                r = m - 1
            else:
                l = m + 1
        return l