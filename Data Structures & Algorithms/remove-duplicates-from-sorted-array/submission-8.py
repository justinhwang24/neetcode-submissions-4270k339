class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for n in nums:
            if n not in seen:
                seen.append(n)
        nums[:] = seen
        return len(seen)