class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # ind, height
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                ind, height = stack.pop()
                maxArea = max(maxArea, (i - ind) * height)
                start = ind
            stack.append((start, heights[i]))
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea