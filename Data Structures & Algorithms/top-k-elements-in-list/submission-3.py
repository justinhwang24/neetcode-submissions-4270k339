class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        heap = []
        for n in nums:
            counts[n] += 1
        for key in counts:
            heapq.heappush(heap, (counts[key], key))
        while len(heap) > k:
            heapq.heappop(heap)
        return [b for a, b in heap]
            