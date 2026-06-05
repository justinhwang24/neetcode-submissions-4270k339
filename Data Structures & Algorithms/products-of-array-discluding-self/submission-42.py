class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            pref[i] = p
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            pref[i] *= p
            p *= nums[i]
        return pref