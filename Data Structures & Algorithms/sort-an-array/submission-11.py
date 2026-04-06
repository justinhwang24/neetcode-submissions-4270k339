class Solution:
    def merge(self, nums, a, m, b):
        leftArr = nums[a : m+1]
        rightArr = nums[m+1 : b+1]
        i, l, r = a, 0, 0
        while l < len(leftArr) and r < len(rightArr):
            if leftArr[l] < rightArr[r]:
                nums[i] = leftArr[l]
                l += 1
            else:
                nums[i] = rightArr[r]
                r += 1
            i += 1
        while l < len(leftArr):
            nums[i] = leftArr[l]
            l += 1
            i += 1
        while r < len(rightArr):
            nums[i] = rightArr[r]
            r += 1
            i += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        def sortArrayHelp(nums, a, b):
            if a >= b:
                return
            m = (a+b) // 2
            sortArrayHelp(nums, a, m)
            sortArrayHelp(nums, m+1, b)
            self.merge(nums, a, m, b)

        sortArrayHelp(nums, 0, len(nums) - 1)
        return nums