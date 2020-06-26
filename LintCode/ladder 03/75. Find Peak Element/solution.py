class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left, right = 0, len(A) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if A[mid] < A[mid + 1]:
                left = mid
            elif A[mid] >= A[mid + 1]:
                right = mid
                
        return left if A[left] > A[right] else right