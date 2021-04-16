class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res = []
        self.search(n, [], res)
        return res
        
    def search(self, n, cols, res):
        row = len(cols)
        if row == n:
            res.append(self.draw_chessboard(cols))
            return
        
        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue
            cols.append(col)
            self.search(n, cols, res)
            cols.pop()
            
    def draw_chessboard(self, cols):
        num_cols = len(cols)
        board = []
        for i in range(num_cols):
            row = ['Q' if j == cols[i] else '.' for j in range(num_cols)]
            board.append(''.join(row))
        return board
        
    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
                
        return True