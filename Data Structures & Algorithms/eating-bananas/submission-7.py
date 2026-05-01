class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = max(piles)
        while l <= r:
            m = (l + r) // 2
            tot = 0
            for i in range(len(piles)):
                tot += -(-piles[i] // m)
            if tot > h:
                l = m + 1
            elif tot <= h:
                r = m - 1
        return l