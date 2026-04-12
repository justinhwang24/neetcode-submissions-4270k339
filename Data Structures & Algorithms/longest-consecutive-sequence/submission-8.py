class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 in numSet:
                continue
            curr = 0
            while n + curr in numSet:
                curr += 1
            longest = max(curr, longest)
        return longest