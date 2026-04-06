class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i in range(len(nums)):
            if nums[i] in need:
                return sorted([i, need[nums[i]]])
            need[target - nums[i]] = i
        return -1