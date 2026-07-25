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
            newNode = Node(cur.val)
            oldToNew[cur] = newNode
            for nbr in cur.neighbors:
                newNode.neighbors.append(dfs(nbr))
            return oldToNew[cur]
        
        return dfs(node) if node else None