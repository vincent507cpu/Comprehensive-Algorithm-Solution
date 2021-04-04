class Solution:
    """
    @param n: An integer.
    @return: A string list.
    """
    def printX(self, n):
        # write your code here.
        res = []

        for i in range(n):
            tmp = [' '] * n
            for j in range(n):
                if i == j or i + j == n - 1:
                    tmp[j] = 'X'
            tmp = ''.join(tmp)
            res.append(tmp)

        return res