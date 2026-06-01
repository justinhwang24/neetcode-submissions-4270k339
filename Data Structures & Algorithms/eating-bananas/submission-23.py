class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            tot = 0
            for p in piles:
                tot -= (-p // m)
            if tot <= h:
                res = m
                r = m - 1
            elif tot > h:
                l = m + 1
        return res