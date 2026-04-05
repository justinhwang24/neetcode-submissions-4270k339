class Solution:
    def isValidSet(self, lst):
        clean = []
        for c in lst:
            if c != ".":
                clean.append(c)
        if len(set(clean)) != len(clean):
            return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidSet(board[i]):
                return False
        
        for i in range(9):
            lst = []
            for j in range(9):
                lst.append(board[j][i])
            if not self.isValidSet(lst):
                return False
        
        for n in range(9):
            lst = []
            for i in range(3 * (n%3), 3 * (n%3) + 3):
                for j in range(3 * (n // 3), 3 * (n // 3) + 3):
                    lst.append(board[i][j])
            if not self.isValidSet(lst):
                return False
        return True