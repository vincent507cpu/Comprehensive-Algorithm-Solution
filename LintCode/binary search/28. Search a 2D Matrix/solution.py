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