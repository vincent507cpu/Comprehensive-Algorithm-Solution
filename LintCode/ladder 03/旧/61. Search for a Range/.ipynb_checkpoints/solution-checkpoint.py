class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
            
        if self.find_boundries(A, target, True) == float('inf'):
            return [-1, -1]
        else:
            left = self.find_boundries(A, target, True)
            right = self.find_boundries(A, target, False)
            return [left, right]
        
    def find_boundries(self, A, target, find_left):
        start, end = 0, len(A) - 1
        
        
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                if find_left == True:
                    end = mid
                else:
                    start = mid
                    
        if find_left == True:
            if A[start] == target:
                return start
            if A[end] == target:
                return end
        else:
            if A[end] == target:
                return end
            if A[start] == target:
                return start
                
        return float('inf')