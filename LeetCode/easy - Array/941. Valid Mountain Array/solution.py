class Solution:
    # my solution
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        idx = A.index(max(A))
        if idx == 0 or idx == len(A) - 1:
            return False
        
        for i in range(idx-1):
            if A[i] >= A[i+1]:
                return False
            
        for i in range(idx, len(A)-1):
            if A[i] <= A[i+1]:
                return False
            
        return True
    
    # better solution
    # https://leetcode.com/problems/valid-mountain-array/discuss/194900/C%2B%2BJavaPython-Climb-Mountain
    '''
    Two people climb from left and from right separately.
    If they are climbing the same mountain,
    they will meet at the same point.
    '''
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        left, right, length = 0, len(A) - 1, len(A)
        
        while left < length - 1 and A[left] < A[left+1]:
            left += 1
            
        while right > 0 and A[right-1] > A[right]:
            right -= 1
            
        return 0 < left == right < length - 1