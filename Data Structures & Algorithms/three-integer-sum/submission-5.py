class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                elif nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    r -= 1
        return res