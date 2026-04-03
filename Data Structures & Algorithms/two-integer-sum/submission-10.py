class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                return sorted([i, diffs[diff]])
            diffs[nums[i]] = i