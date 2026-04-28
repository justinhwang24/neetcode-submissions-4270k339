class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and n < 0 and stack[-1] > 0:
                diff = n + stack[-1]
                if diff > 0:
                    n = 0
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    n = 0
            if n != 0:
                stack.append(n)
        return stack