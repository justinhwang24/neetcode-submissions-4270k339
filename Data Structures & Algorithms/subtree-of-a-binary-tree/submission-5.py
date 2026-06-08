# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(treeA, treeB):
            if not treeA and not treeB:
                return True
            if treeA and treeB and treeA.val == treeB.val:
                return sameTree(treeA.left, treeB.left) and sameTree(treeA.right, treeB.right)
            return False
        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)