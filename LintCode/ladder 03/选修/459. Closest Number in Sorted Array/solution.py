class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A: return -1
        
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                return mid

        if A[end] - target > target - A[start]:
            return start
        else:
            return end