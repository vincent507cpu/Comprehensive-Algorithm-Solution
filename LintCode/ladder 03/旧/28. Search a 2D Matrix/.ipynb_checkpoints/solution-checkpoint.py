class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        row = len(matrix)
        col = len(matrix[0])
        
        start, end = 0, row * col - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.getIdx(matrix, mid) < target:
                start = mid
            elif self.getIdx(matrix, mid) > target:
                end = mid
            else:
                return True
                
        if self.getIdx(matrix, start) == target:
            return True
            
        if self.getIdx(matrix, end) == target:
            return True
            
        return False
            
    def getIdx(self, matrix, idx):
        row = idx // len(matrix[0])
        col = idx % len(matrix[0])
        
        return matrix[row][col]