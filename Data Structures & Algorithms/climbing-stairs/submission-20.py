class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1
        for i in range(n - 1):
            temp = prev
            prev += cur
            cur = temp
        return prev