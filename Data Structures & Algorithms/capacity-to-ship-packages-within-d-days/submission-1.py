class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l + r) // 2
            i = 0
            tot = 1
            rem = m
            while i < len(weights):
                if weights[i] <= rem:
                    rem -= weights[i]
                else:
                    tot += 1
                    rem = m - weights[i]
                i += 1
            if tot <= days:
                r = m - 1
            else:
                l = m + 1
        return l