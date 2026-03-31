class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        last_worked = -1 
        while left <= right:
            m = (left + right) // 2
            tot = 0
            for pile in piles:
                tot += -(-pile // m)
            if tot <= h:
                last_worked = m
                right = m - 1
            elif tot > h:
                left = m + 1

        return last_worked