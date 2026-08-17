class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_copy = [-i for i in stones]
        heapq.heapify(stones_copy)
        while len(stones_copy) > 1:
            x = -heapq.heappop(stones_copy)
            y = -heapq.heappop(stones_copy)
            if y < x:
                heapq.heappush(stones_copy, -(x - y))
        return -stones_copy[0] if stones_copy else 0