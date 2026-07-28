# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque()
        q.append((root, -float('inf'), float('inf')))
        while q:
            cur, left, right = q.popleft()
            if not (left < cur.val < right):
                return False
            if cur.left:
                q.append((cur.left, left, cur.val))
            if cur.right:
                q.append((cur.right, cur.val, right))
        
        return True