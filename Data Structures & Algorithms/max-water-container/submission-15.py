class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            if heights[l] <= heights[r]:
                maxVol = max(maxVol, (r - l) * heights[l])
                l += 1
            else:
                maxVol = max(maxVol, (r - l) * heights[r])
                r -= 1
        return maxVol
            