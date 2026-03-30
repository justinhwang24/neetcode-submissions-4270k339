class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = -1
        for i in range(n - 1, -1, -1):
            t = max(arr[i], mx)
            arr[i] = mx
            mx = t
        return arr