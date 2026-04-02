# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        n = root.val
        if not root.left and not root.right:
            return targetSum == n
        if not root.left:
            return self.hasPathSum(root.right, targetSum - n)
        elif not root.right:
            return self.hasPathSum(root.left, targetSum - n)
        else:
            return self.hasPathSum(root.left, targetSum - n) \
                or self.hasPathSum(root.right, targetSum - n)