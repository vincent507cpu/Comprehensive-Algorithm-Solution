# insertion sort

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(len(A)):
            min_idx = i
            for j in range(i, len(A)):
                if A[j] < A[min_idx]:
                    min_idx = j
            if min_idx != i:
                A[i], A[min_idx] = A[min_idx], A[i]