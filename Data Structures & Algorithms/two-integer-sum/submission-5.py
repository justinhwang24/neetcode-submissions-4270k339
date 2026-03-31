class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                j = diffs[target - nums[i]]
                return [min(i,j), max(i,j)]
            diffs[nums[i]] = i
        return []