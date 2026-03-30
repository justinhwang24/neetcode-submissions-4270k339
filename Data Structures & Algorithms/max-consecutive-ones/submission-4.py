class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                if curr > maximum:
                    maximum = curr
                curr = 0
        if curr > maximum:
            maximum = curr
        return maximum
