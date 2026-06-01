class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l + r) // 2
            k = 1
            temp = 0
            for i in weights:
                temp += i
                if temp > m:
                    temp = i
                    k += 1
            if k <= days:
                r = m - 1
            elif k > days:
                l = m + 1
        return l