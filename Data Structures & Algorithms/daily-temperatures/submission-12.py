class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temp, i)
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((n, i))
        return res