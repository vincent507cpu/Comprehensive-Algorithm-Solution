class Solution:
    # my solution
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
                
        return True
    
    # recursion
    # https://leetcode.com/problems/toeplitz-matrix/discuss/602909/Simple-Recursion-or-Python-or-Faster-than-96.44
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        
        for i in range(len(matrix)-1):
            if matrix[i][0] != matrix[i+1][1]:
                return False
        
        for i in range(len(matrix[0])-1):
            if matrix[0][i] != matrix[1][i+1]:
                return False
            
        return self.isToeplitzMatrix([x[1:] for x in matrix])