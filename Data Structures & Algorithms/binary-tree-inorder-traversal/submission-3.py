# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversalHelp(root, [])

    def inorderTraversalHelp(self, root: Optional[TreeNode], lst) -> List[int]:
        if not root:
            return lst
        self.inorderTraversalHelp(root.left, lst)
        lst.append(root.val)
        self.inorderTraversalHelp(root.right, lst)
        return lst