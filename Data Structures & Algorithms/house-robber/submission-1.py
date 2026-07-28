class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for num in nums:
            temp = max(num + prev, cur)
            prev = cur
            cur = temp
        
        return cur