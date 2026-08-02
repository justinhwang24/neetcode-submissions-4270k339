class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pac, atl = set(), set()

        def dfs(r, c, visit, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit:
                return False
            if heights[r][c] < prev:
                return False
            visit.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        res = []
        for r in range(ROWS):
            if dfs(r, 0, pac, -1):
                res.append(r, 0)
        for c in range(COLS):
            if dfs(0, c, pac, -1):
                res.append(0, c)
        for r in range(ROWS):
            if dfs(r, COLS - 1, atl, -1):
                res.append(r, COLS - 1)
        for c in range(COLS):
            if dfs(ROWS - 1, c, atl, -1):
                res.append(ROWS - 1, c)
        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])
        return res