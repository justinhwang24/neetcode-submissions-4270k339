class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = -1
        count = 0
        for n in nums:
            if count == 0:
                curr = n
            if n == curr:
                count += 1
            else:
                count -= 1
        
        return curr