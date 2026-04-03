# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curr, tot):
            if not curr:
                return False
            tot += curr.val
            if not curr.left and not curr.right:
                return tot == targetSum

            return dfs(curr.left, tot) or dfs(curr.right, tot)
        
        return dfs(root, 0)
            