class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for n in nums:
            temp = max(prev + n, cur)
            prev = cur
            cur = temp
        return cur