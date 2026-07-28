class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(cur):
            visit.add(cur)
            for nbr in adj[cur]:
                if nbr not in visit:
                    dfs(nbr)
        
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        
        return res
