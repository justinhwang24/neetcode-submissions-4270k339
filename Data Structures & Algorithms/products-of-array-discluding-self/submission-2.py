class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], [1]
        left, right = 1, 1
        for i in range(len(nums)):
            if i > 0:
                left *= nums[i - 1]
                prefix.append(left)
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                right *= nums[i + 1]
                suffix.append(right)
        suffix.reverse()
        return [prefix[i] * suffix[i] for i in range(len(nums))]