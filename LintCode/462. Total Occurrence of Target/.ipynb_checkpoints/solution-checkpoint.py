class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
            
        right = self.findBandries(A, target, 0, len(A) - 1, findLeft = False) 
        left = self.findBandries(A, target, 0, len(A) - 1) 
        
        if left == 0 and right == 0:
            return 0
        return right - left + 1
        
    def findBandries(self, A, target, start, end, findLeft = True):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                if findLeft:
                    end = mid
                else:
                    start = mid
        
        if findLeft: 
            if A[start] == target:
                return start
            if A[end] == target:
                return end
            return 0
        else:
            if A[end] == target:
                return end
            if A[start] == target:
                return start
            return 0