class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:]
        right = nums2[:]
        i = 0
        j = 0
        count = 0
        while i < m and j < n:
            if left[i] <= right[j]:
                nums1[count] = left[i]
                i += 1
            else:
                nums1[count] = right[j]
                j += 1
            count += 1
        while i < m:
            nums1[count] = left[i]
            i += 1
            count += 1
        while j < n:
            nums1[count] = right[j]
            j += 1
            count += 1
          