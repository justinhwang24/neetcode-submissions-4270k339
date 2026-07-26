"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(cur):
            if cur in oldToNew:
                return oldToNew[cur]
            copy = Node(cur.val)
            oldToNew[cur] = copy
            for child in cur.neighbors:
                copy.neighbors.append(dfs(child))
            return copy
        
        if not node:
            return
        return dfs(node)