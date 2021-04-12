class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A: return B
        if not B: return A

        i, j, res = 0, 0, []

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1

        while i < len(A):
            res.append(A[i])
            i += 1

        while j < len(B):
            res.append(B[j])
            j += 1

        return res