class Solution:
    # brute force
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if min(matrix[i]) == matrix[i][j] and max(matrix[k][j] for k in range(len(matrix))) == matrix[i][j]:
                    res += [matrix[i][j]]
                    
        return res
    
    # hash
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = set(min(row) for row in matrix)
        col = set(max(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))
        return list(row.intersection(col))