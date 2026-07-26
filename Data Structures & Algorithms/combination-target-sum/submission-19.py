class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, lst, total):
            if total == target:
                res.append(lst.copy())
                return 
            if total > target or i >= len(nums):
                return
            lst.append(nums[i])
            dfs(i, lst, total + nums[i])
            lst.remove(nums[i])
            dfs(i + 1, lst, total)
        
        dfs(0, [], 0)
        return res