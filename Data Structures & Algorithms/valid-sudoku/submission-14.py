class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].append(val)
                    cols[c].append(val)
                    squares[(r // 3, c // 3)].append(val)
        
        for r in range(9):
            for c in range(9):
                if len(rows[r]) != len(set(rows[r])) or \
                    len(cols[c]) != len(set(cols[c])) or \
                    len(squares[(r // 3, c // 3)]) != \
                    len(set(squares[(r // 3, c // 3)])):
                    return False
        return True