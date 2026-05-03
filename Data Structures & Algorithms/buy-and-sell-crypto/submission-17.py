class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = max(prices)
        for i in range(len(prices)):
            res = max(res, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return res
            