class Solution:
    """
    @param A: An integer
    @return: a float number
    """
    def maxOfArray(self, A):
        # write your code here
        res = float('-inf')

        for num in A:
            if num > res:
                res = num

        return res