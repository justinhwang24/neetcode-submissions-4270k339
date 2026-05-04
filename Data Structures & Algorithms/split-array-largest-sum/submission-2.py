class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = n
            return True
        
        l = max(nums)
        r = sum(nums)
        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                r = m - 1
            else:
                l = m + 1
        return l