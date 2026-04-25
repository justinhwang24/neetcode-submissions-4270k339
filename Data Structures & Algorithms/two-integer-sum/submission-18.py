class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in find:
                find[target - n] = i
            else:
                return [find[n], i]