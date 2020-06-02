class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    # two pointers
    def mergeSortedArray(self, A, B):
        # write your code here
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
                
        if A[i:]:
            return res + A[i:]
        else:
            return res + B[j:]