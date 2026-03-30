class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                maximum = max(maximum, curr)
                curr = 0
        return max(maximum, curr)
