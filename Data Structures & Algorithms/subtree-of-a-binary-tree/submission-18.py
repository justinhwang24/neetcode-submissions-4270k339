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
            if rootA and rootB and rootA.val == rootB.val:
                return sameTree(rootA.left, rootB.left) and sameTree(rootA.right, rootB.right)
            return False
        
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur:
                if sameTree(cur, subRoot):
                    return True
                q.append(cur.left)
                q.append(cur.right)
        return False