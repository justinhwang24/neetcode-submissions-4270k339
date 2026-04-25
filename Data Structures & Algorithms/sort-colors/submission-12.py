class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1
        i = 0
        for j in range(3):
            k = 0
            while k < counts[j]:
                nums[i] = j
                i += 1
                k += 1
        return nums