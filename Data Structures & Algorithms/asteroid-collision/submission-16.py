class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and stack[-1] > 0 and n < 0:
                diff = stack[-1] + n
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    n = 0
                else:
                    stack.pop()
                    n = 0
            if n != 0:
                stack.append(n)
        return stack