class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dist = x**2 + y**2
            dists.append((dist, x, y))
        heapq.heapify(dists)
        res = []
        while k > 0:
            t = heapq.heappop(dists)
            res.append([t[1], t[2]])
            k -= 1
        return res