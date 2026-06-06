class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        numFreq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, v in count.items():
            numFreq[v].append(n)
        res = []
        for i in range(len(nums), -1, -1):
            for n in numFreq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res