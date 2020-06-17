class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        n, m = len(image), len(image[0])
        
        left = self.findFirst(image, 0, y, self.checkCol)
        right = self.findLast(image, y, m - 1, self.checkCol)
        up = self.findFirst(image, 0, x, self.checkRow)
        down = self.findLast(image, x, n - 1, self.checkRow)
        
        return (right - left + 1) * (down - up + 1)
        
    def findFirst(self, image, start, end, chechFunc):
        while start + 1 < end:
            mid = (start + end) // 2
            if chechFunc(image, mid):
                end = mid
            else:
                start = mid
        if chechFunc(image, start):
            return start
        return end
        
    def findLast(self, image, start, end, chechFunc):
        while start + 1 < end:
            mid = (start + end) // 2
            if chechFunc(image, mid):
                start = mid
            else:
                end = mid
        if chechFunc(image, end):
            return end
        return start
        
    def checkCol(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False
        
    def checkRow(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True
        return False