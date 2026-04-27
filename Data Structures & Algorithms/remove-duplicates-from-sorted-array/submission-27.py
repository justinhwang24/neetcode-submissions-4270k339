class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        k = 1
        while l < len(nums):
            if nums[l] != nums[l - 1]:
                nums[k] = nums[l]
                k += 1
            l += 1
        return k