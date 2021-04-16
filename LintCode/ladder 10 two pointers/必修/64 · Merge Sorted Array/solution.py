class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        while n:
            if m and A[m - 1] > B[n - 1]:
                A[m + n -1] = A[m - 1]
                m -= 1
            else:
                A[m + n -1] = B[n - 1]
                n -= 1