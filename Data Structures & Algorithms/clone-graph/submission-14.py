"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nbr in cur.neighbors:
                if nbr not in oldToNew:
                    oldToNew[nbr] = Node(nbr.val)
                    q.append(nbr)
            
                oldToNew[cur].neighbors.append(oldToNew[nbr])
        
        return oldToNew[node]