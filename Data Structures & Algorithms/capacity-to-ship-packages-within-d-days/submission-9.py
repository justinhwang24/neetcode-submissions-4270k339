class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l + r) // 2
            tot = 1
            cur = 0
            for i in weights:
                cur += i
                if cur > m:
                    tot += 1
                    cur = i
            if tot <= days:
                r = m - 1
            else:
                l = m + 1
        return l
