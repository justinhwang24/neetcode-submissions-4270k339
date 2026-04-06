class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = 0
        currMax = currMin = 0
        for i in range(len(nums)):
            currMin = min(0, currMin)
            currMax = max(0, currMax)
            currMin += nums[i]
            currMax += nums[i]
            minSum = min(currMin, minSum)
            maxSum = max(currMax, maxSum)
        if maxSum > 0:
            return max(maxSum, sum(nums) - minSum)
        return maxSum