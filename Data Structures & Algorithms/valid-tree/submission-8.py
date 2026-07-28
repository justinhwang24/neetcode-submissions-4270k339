class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(cur, par):
            if cur in visit:
                return False
            visit.add(cur)
            for nbr in adj[cur]:
                if nbr == par:
                    continue
                if not dfs(nbr, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
                