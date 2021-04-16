class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        start, end = 0, len(matrix) * len(matrix[0]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get(mid, matrix) < target:
                start = mid
            elif self.get(mid, matrix) > target:
                end = mid
            else:
                return True

        if self.get(start, matrix) == target:
            return True
        if self.get(end, matrix) == target:
            return True
        return False

    def get(self, idx, matrix):
        row = idx // len(matrix[0])
        col = idx % len(matrix[0])

        return matrix[row][col]