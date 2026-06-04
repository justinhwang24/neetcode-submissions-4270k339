class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l <= r:
            if heights[l] <= heights[r]:
                maxArea = max(maxArea, heights[l] * (r - l))
                l += 1
            else:
                maxArea = max(maxArea, heights[r] * (r - l))
                r -= 1
        return maxArea