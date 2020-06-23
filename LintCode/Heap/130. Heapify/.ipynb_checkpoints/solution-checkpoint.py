# sift down

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A) - 1, -1, -1):
            self.siftdown(A, i)
            
    def siftdown(self, A, k):
        while 2 * k + 1 < len(A):
            son = 2 * k + 1
            if 2 * k + 2 < len(A) and A[son] > A[2 * k + 2]:
                son = 2 * k + 2
            if A[son] >= A[k]:
                break
            
            A[son], A[k] = A[k], A[son]
            k = son