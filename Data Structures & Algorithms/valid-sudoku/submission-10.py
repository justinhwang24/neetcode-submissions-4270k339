class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        boxes = defaultdict(list)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                cols[j].append(val)
                rows[i].append(val)
                boxes[3 * (i // 3) + j // 3].append(val)
        for i in range(9):
            if len(cols[i]) != len(set(cols[i])) \
                or len(rows[i]) != len(set(rows[i])) \
                or len(boxes[i]) != len(set(boxes[i])):
                return False
        return True