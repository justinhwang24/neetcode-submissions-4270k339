class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            if nums[i] in diffs:
                j = diffs[nums[i]]
                return sorted([i, j])
            diffs[target - nums[i]] = i