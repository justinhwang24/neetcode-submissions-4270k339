class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        res = []
        for i in range(len(nums) - 1):
            pref.append(pref[-1] * nums[i])
        for i in range(len(nums) - 1, 0, -1):
            suff.append(suff[-1] * nums[i])
        suff.reverse()
        for i in range(len(nums)):
            res.append(pref[i] * suff[i])
        return res