class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return -1
            
        row, start, end = 0, 0, len(matrix[0]) - 1
        
        while row < len(matrix) - 1:
            if matrix[row][end] >= target:
                break
            else:
                row += 1
                
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid
            elif matrix[row][mid] > target:
                end = mid
            else:
                return True
                
        if matrix[row][start] == target or matrix[row][end] == target:
            return True
            
        return False
    
    # convert to a 1D array
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or len(matrix[0]) == 0:
            return False
            
        m, n = len(matrix), len(matrix[0])
        
        start, end = 0, m * n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get(matrix, mid) < target:
                start = mid
            else:
                end = mid
                
        if self.get(matrix, start) == target or self.get(matrix, end) == target:
            return True
        
        return False
        
    def get(self, matrix, idx):
        row = idx // len(matrix[0])
        col = idx % len(matrix[0])
        return matrix[row][col]