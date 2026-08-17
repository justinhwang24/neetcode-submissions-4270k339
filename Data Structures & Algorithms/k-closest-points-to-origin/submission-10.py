class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            dists.append((dist, point[0], point[1]))
        heapq.heapify(dists)
        res = []
        for i in range(k):
            t = heapq.heappop(dists)
            res.append([t[1], t[2]])
        return res