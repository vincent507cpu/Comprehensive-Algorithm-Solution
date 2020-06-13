class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m, n = len(matrix), len(matrix[0])
        
        x, y = m - 1, 0
        res = 0
        
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                x -= 1
                y += 1
                res += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
                
        return res