class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(a, b):
            if a > b:
                return -1
            i = (a + b) // 2
            if nums[i] < target:
                return binarySearch(i + 1, b)
            elif nums[i] > target:
                return binarySearch(a, i - 1)
            else:
                return i

        return binarySearch(0, len(nums) - 1)