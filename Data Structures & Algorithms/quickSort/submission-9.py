# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortHelp(pairs, a, b):
            if b <= a:
                return pairs
            pivot = pairs[b]
            i = a
            for j in range(a, b):
                if pairs[j].key < pivot.key:
                    temp = pairs[i]
                    pairs[i] = pairs[j]
                    pairs[j] = temp
                    i += 1
            pairs[b] = pairs[i]
            pairs[i] = pivot
            
            quickSortHelp(pairs, a, i - 1)
            quickSortHelp(pairs, i + 1, b)
        
        quickSortHelp(pairs, 0, len(pairs) - 1)
        return pairs