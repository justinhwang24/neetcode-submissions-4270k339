class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        n = nums.pop()
        res = []
        for lst in self.subsets(nums):
            res.append(lst)
            temp = lst[:]
            temp.append(n)
            res.append(temp)
        return res