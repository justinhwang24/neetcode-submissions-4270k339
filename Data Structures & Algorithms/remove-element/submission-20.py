class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[curr]
                nums[curr] = nums[i]
                nums[i] = temp
                curr += 1
        return curr