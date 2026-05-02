class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            m = (l + r) // 2
            time = 0
            for i in piles:
                time += -(-i // m)
            if time <= h:
                r = m - 1
            elif time > h:
                l = m + 1
        return l
