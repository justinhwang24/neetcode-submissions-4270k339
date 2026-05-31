class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        stack = []

        for pos, sp in pairs:
            time = (target - pos) / sp
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)