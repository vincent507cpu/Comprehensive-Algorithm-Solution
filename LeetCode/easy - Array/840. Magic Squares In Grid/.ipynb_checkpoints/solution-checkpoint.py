# https://leetcode.com/problems/magic-squares-in-grid/discuss/208894/Python-Solution

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        # Construct the 3x3 square
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                tmp = [grid[i+k][j:j+3] for k in range(3)]
                if self.isMagicSquare(tmp):
                    res += 1
                    
        return res
        
    
    def isMagicSquare(self, grid):
        '''
        Check whether the given grid is a magic square
        '''
        # Check the elements
        flat = [num for row in grid for num in row]
        if sorted(flat) != list(range(1, 10)):
            return False
        
        # Check the row, column and diagnal sums
        row = [sum(row) for row in grid]
        col = [sum([row[i] for row in grid]) for i in range(3)]
        diag = [grid[0][0]+grid[1][1]+grid[2][2], grid[0][2]+grid[1][1]+grid[2][0]]

        row.extend(col)
        row.extend(diag)
        
        return len(set(row)) == 1