class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            if nums[i] not in diffs:
                diffs[target - nums[i]] = i
            else:
                j = diffs[nums[i]]
                return sorted([i, j])
        return [-1, -1]