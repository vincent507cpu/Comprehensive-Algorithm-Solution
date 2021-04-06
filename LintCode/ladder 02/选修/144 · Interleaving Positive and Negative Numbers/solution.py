class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        if not A or len(A) < 2:
            return A

        pos, neg = 0, 0

        for n in A:
            if n < 0:
                neg += 1
            else:
                pos += 1

        if neg > pos:
            negIdx, posIdx = 0, 1
        else:
            negIdx, posIdx = 1, 0

        while posIdx < len(A) and negIdx < len(A):
            while negIdx < len(A) and A[negIdx] < 0:
                negIdx += 2

            while posIdx < len(A) and A[posIdx] > 0:
                posIdx += 2

            if posIdx < len(A) and negIdx < len(A):
                A[posIdx], A[negIdx] = A[negIdx], A[posIdx]

                posIdx += 2
                negIdx += 2