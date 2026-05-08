class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            aL = a[i] if i >= 0 else float("-infinity")
            aR = a[i + 1] if i + 1 < len(a) else float("infinity")
            bL = b[j] if j >= 0 else float("-infinity")
            bR = b[j + 1] if j + 1 < len(b) else float("infinity")
            
            if aL <= bR and bL <= aR:
                if total % 2:
                    return min(aR, bR)
                return (max(aL, bL) + min(aR, bR)) / 2
            elif aL > bR:
                r = i - 1
            else:
                l = i + 1