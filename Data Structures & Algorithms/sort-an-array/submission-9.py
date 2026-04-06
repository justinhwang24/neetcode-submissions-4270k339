class Solution:
    def merge(self, arr, a, m, b):
        left, right = arr[a:m+1], arr[m+1:b+1]
        i, l, r = a, 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1
        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        def sortArrayHelp(arr, a, b):
            if a >= b:
                return
            m = (a + b) // 2
            sortArrayHelp(arr, a, m)
            sortArrayHelp(arr, m + 1, b)
            self.merge(nums, a, m, b)

        sortArrayHelp(nums, 0, len(nums) - 1)
        return nums