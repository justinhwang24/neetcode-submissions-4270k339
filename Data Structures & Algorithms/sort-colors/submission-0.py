class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * (max(nums) + 1)
        for n in nums:
            counts[n] += 1
        curr = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[curr] = i
                curr += 1