# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(rootA, rootB):
            if not rootA and not rootB:
                return True
            if not rootA or not rootB:
                return False
            return rootA.val == rootB.val and sameTree(rootA.left, rootB.left) and sameTree(rootA.right, rootB.right)
        if not root and not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)