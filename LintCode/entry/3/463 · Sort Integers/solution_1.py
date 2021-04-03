# bubble sort

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]