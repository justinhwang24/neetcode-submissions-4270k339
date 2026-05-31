class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxVol = 0
        while l <= r:
            if heights[l] <= heights[r]:
                maxVol = max((r - l) * heights[l], maxVol)
                l += 1
            else:
                maxVol = max((r - l) * heights[r], maxVol)
                r -= 1
        return maxVol