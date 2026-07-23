class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(lst, curSum, i):
            if curSum == target:
                res.append(lst.copy())
                return
            elif i >= len(nums) or curSum > target:
                return
            else:
                lst.append(nums[i])
                dfs(lst, curSum + nums[i], i)
                lst.pop()
                dfs(lst, curSum, i + 1)
        
        dfs([], 0, 0)
        return res