class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        seen = -101
        while i < len(nums):
            if nums[i] != seen:
                nums[j] = nums[i]
                j += 1
                seen = nums[i]
            i += 1
        return j