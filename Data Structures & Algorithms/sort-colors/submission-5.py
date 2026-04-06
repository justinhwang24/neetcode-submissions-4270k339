class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        i = 0
        for j in nums:
            counts[j] += 1
        for j in range(3):
            for k in range(counts[j]):
                nums[i] = j
                i += 1