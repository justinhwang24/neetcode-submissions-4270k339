class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                boxes[(r // 3, c // 3)].append(board[r][c])

                if len(rows[r]) != len(set(rows[r])) or \
                len(cols[c]) != len(set(cols[c])) or \
                len(boxes[(r // 3, c // 3)]) != len(set(boxes[(r // 3, c // 3)])):
                    return False
        return True
        