# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if node1 and node2 and node1.val == node2.val:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            else:
                return False
        return True