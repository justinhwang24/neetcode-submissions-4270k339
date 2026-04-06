class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        curr1 = curr2 = -1
        count1 = count2 = 0
        for n in nums:
            if n == curr1:
                count1 += 1
            elif n == curr2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                curr1 = n
            elif count2 == 0:
                count2 = 1
                curr2 = n
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for n in nums:
            if n == curr1:
                count1 += 1
            elif n == curr2:
                count2 += 1
        res = []
        if count1 > len(nums) // 3:
            res.append(curr1)
        if count2 > len(nums) // 3:
            res.append(curr2)

        return res