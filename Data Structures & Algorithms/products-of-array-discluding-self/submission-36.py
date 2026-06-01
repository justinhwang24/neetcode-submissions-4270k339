class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            pref[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            pref[i] *= tmp
            tmp *= nums[i]
        return pref