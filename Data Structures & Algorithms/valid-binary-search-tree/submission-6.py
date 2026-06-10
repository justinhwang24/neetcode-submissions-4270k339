# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(cur, left, right):
            if not cur:
                return True
            if left < cur.val < right:
                return isValid(cur.left, left, cur.val) and \
                    isValid(cur.right, cur.val, right)
            return False
        
        return isValid(root, float("-inf"), float("inf"))