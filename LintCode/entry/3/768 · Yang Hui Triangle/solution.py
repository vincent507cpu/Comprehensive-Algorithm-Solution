class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """
    def calcYangHuisTriangle(self, n):
        # write your code here
        if not n:
            return []
        res = [[1]]

        for _ in range(2, n+1):
            tmp1 = [0] + res[-1]
            tmp2 = res[-1] + [0]
            res.append([a + b for a, b in zip(tmp1, tmp2)])
            
        return res