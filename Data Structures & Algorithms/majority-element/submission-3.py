class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for k, v in counts.items():
            if v >= len(nums) // 2:
                return k
        return nums[0]