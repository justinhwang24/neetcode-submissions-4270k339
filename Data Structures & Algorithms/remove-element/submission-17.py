class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[curr]
                nums[curr] = temp
                curr += 1
        return curr