class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        visit.add(0)
        q = deque()
        q.append((0, -1))

        while q:
            cur, par = q.popleft()
            for nbr in adj[cur]:
                if nbr == par:
                    continue
                if nbr in visit:
                    return False
                visit.add(nbr)
                q.append((nbr, cur))
        
        return len(visit) == n
                