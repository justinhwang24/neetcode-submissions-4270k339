# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelp(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelp(self, pairs: List[Pair], a: int, b: int) -> List[Pair]:
        if b <= a:
            return pairs
        
        m = (a + b) // 2
        self.mergeSortHelp(pairs, a, m)
        self.mergeSortHelp(pairs, m + 1, b)
        self.merge(pairs, a, m, b)
        return pairs
    
    def merge(self, pairs, a, m, b):
        left = pairs[a : m+1]
        right = pairs[m+1 : b+1]
        curr = a
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[curr] = left[i]
                i += 1
            else:
                pairs[curr] = right[j]
                j += 1
            curr += 1
        while i < len(left):
            pairs[curr] = left[i]
            i += 1
            curr += 1
        while j < len(right):
            pairs[curr] = right[j]
            j += 1
            curr += 1