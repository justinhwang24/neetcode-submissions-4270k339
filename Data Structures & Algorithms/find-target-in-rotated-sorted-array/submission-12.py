class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(a, b):
            while a <= b:
                m = (a + b) // 2
                if target < nums[m]:
                    b = m - 1
                elif target > nums[m]:
                    a = m + 1
                else:
                    return m
            return -1

        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        pivot = l

        res = binary_search(0, pivot - 1)
        if res != -1:
            return res
        return binary_search(pivot, len(nums) - 1)