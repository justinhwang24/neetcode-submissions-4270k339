class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res1 = res2 = -1
        count1 = count2 = 0
        for n in nums:
            if n == res1:
                count1 += 1
            elif n == res2:
                count2 += 1
            elif count1 == 0:
                res1 = n
                count1 = 1
            elif count2 == 0:
                res2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for n in nums:
            if n == res1:
                count1 += 1
            elif n == res2:
                count2 += 1
        
        res = []
        if count1 > len(nums) // 3:
            res.append(res1)
        if count2 > len(nums) // 3:
            res.append(res2)
        return res